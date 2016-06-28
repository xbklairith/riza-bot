"""
Conversation generator module
@author Tao PR (github.com/starcolon)
CopyRight 2016-present
"""

import os
import sys
import getpass
from termcolor import colored
from conversation.flow import TalkFlow
from conversation.botinteraction import BotInteractionModel
from bot.bot import Bot 
from data.userquery import UserQuery
from data.userquery import UserQueryEntry
from data.conversation import Conversation
from data.conversation import DialogEntry
from text import texthasher as H
from text import tokeniser as T
from ml import intentclassifier as I

"""
Read on/off commandline arguments
"""
arguments = sys.argv[1:]

# Indicate whether the bot is learning to answer appropriately
is_learning = 'learn' in arguments

"""
Print out colourised text
@param {Tuple} tuples of text and color
"""
def stdout(*argv):
  output = ''
  for txt,color in argv:
    output += colored(txt,color)
  print(colored(txt,color))


"""
Initialise all necessary objects to start a bot.
"""
def init_bot(model_dir):
  botmodel     = BotInteractionModel(alpha=0.3)
  talkflow     = TalkFlow()
  intent_model = I.safe_load(model_dir + '/intent.model')
  text_hasher  = H.safe_load(
    model_dir + '/texthash.model',
    250,
    [],
    'LDA'
  )
  bot = Bot(I,T)
  bot.add_intent_clf(intent_model)
  bot.add_bot_model(botmodel)
  bot.add_talk_flow(talkflow)
  bot.add_text_hasher(text_hasher)
  return bot

def prompt_user_query(bot,datasource_conv,datasource_query):
  stdout(('😧 You say :','magenta'))
  q                    = input()
  uq                   = bot.add_input(q)
  (_,intent,params,_q) = uq

  _intent = intent

  # Ask the user to correct the intent
  # if running in learning mode
  if is_learning:
    stdout(('   Bot believes you mean: ','cyan') , (intent,None))
    if input(colored('   Is that correct (y/n) ? ','cyan')).strip() == 'n':
      # User indicates the extracted intent was not correct.
      _intent = input(colored('  Please correct me : ','yellow'))

    # Add the annotated query to the query dataset
    entry = UserQueryEntry(
      getpass.getuser(),
      q, _intent, params
    )
    entry.add_to(datasource_query)

  # Log the conversation
  dialog = DialogEntry(
    bot.uuid, 
    getpass.getuser(),
    q, _intent, params
  )
  dialog.add_to(datasource_conv)

def generate_response(bot):
  intent,params,resp = bot.generate_response()
  stdout(('👽 Bot says :','green'),(resp,None))

  _resp   = resp
  _intent = intent
  
  # If running in learning mode, 
  # let the user educates the bot what should be 
  # the most appropriate response
  if is_learning:
    stdout(('   Bot just meant : ','cyan'),(intent,None))
    if input(colored('   Is this correct (y/n) ? ','cyan')).strip() == 'n':
      _resp   = input(colored('  So what sentence should I respond? : ','yellow'))
      _intent = input(colored('  And what does it mean? : ', 'yellow'))

  # Log the conversation
  dialog = DialogEntry(
    bot.uuid,
    'bot',
    _resp, _intent, params
  )
  dialog.add_to(datasource_conv)

if __name__ == '__main__':

  # Initialise all data sources
  stdout(('Initialising data sources...','cyan'))
  datasource_query = UserQuery('localhost','riza')
  datasource_conv  = Conversation('localhost','riza')

  # Initialise a bot instance
  stdout(('Initialising bot...','cyan'))
  bot = init_bot('../data/models/')

  # Let the user start a conversation
  prompt_user_query(bot,datasource_conv,datasource_query)
  pass

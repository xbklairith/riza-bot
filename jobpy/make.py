"""
Conversation training set maker
@author Tao PR (github.com/starcolon)
CopyRight 2016-present
"""

import os
import sys
import uuid
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
Print out colourised text
@param {Tuple} tuples of text and color
"""
def stdout(*argv):
  output = ''
  for txt,color in argv:
    output += colored(txt,color)
  print(colored(txt,color))


def prompt_user_query(uuid,datasource_conv,datasource_query):
  q      = input(colored('😧 You say :','magenta'))
  intent = input(colored('😧 What intent it implies? : ', 'magenta'))
  params = []

  # Log the conversation
  dialog = DialogEntry(
    getpass.getuser(),
    q, intent, params
  )
  dialog.add_to(uuid,datasource_conv)

def prompt_bot_response(uuid,datasource_conv,datasource_query):
  q      = input(colored('👽 What should I say :','cyan'))
  intent = input(colored('👽 What intent it implies? : ', 'cyan'))
  params = []
  # Log the conversation
  dialog = DialogEntry(
    'bot',
    q, intent, params
  )
  dialog.add_to(uuid,datasource_conv)

if __name__ == '__main__':
  # Initialise all data sources
  stdout(('Initialising data sources...','cyan'))
  datasource_query = UserQuery('localhost','riza')
  datasource_conv  = Conversation('localhost','riza')

  # Initialise a conversation UUID
  uuid = str(uuid.uuid1())

  # TAOTODO: List all registered intents
  while True:
    prompt_user_query(uuid,datasource_conv,datasource_query)
    prompt_bot_response(uuid,datasource_conv,datasource_query)



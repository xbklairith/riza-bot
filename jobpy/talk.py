"""
Conversation generator module
@author Tao PR (github.com/starcolon)
CopyRight 2016-present
"""

import os
import sys
import argparse
from termcolor import colored
from conversation.botinteraction import BotInteractionModel
from bot.bot import Bot 
from data import userquery as UQ
from text import texthasher as H
from text import tokeniser as T
from ml import intentclassifier as I

arguments = argparse.ArgumentParser()
arguments.add_argument('--d', type=int, default=800) # Dimension of preprocess text hasher
args = vars(arguments.parse_args(sys.argv[1:]))

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
  bot.add_text_hasher(text_hasher)
  return bot

def prompt_user_query(bot):
  stdout(('😧 You say :','magenta'))
  q = input()
  bot.add_input(q)

def generate_response(bot):
  intent,params,resp = bot.generate_response()
  stdout(('👽 Bot says :','green'),(resp,None))
  # TAOTODO: Generate a logical response
  pass

if __name__ == '__main__':
  stdout('Initialising bot...','cyan')
  bot = init_bot('../data/models/')
  prompt_user_query(bot)
  pass

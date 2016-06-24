"""
Bot engine
@author Tao PR (github.com/starcolon)
CopyRight 2016-present
"""

import numpy as np
import os.path
import pickle
import json
from termcolor import colored

class Bot:
  # Initialise the bot, and having required modules
  # injected in
  def __init__(self,IntentClf,TextHash):
    self.IntentClf    = IntentClf
    self.TextHash     = TextHash
    self.conversation = []

  """
  Register an intent classifier model
  """
  def add_intent_clf(self,clf):
    self.clf     = clf
    self._intent = self.IntentClf.classify(self.clf)
    self._train  = self.IntentClf.train(self.clf)

  """
  Register a bot interaction model
  """
  def add_bot_model(self,model):
    self.model = model

  """
  Register a text vectoriser model (hasher)
  """
  def add_text_hasher(self,t):
    self.hasher = t
    self._hash  = self.TextHash(self.hasher,learn=True)

  """
  Given an input, extract a probable intent with arguments
  """
  def extract_intent(self,phrase):
    vs     = self._hash([phrase])
    intent = self._intent(vs)
    return intent

  """
  Add a user input (as a state in the conversation model)
  """
  def add_input(self,user_intent,params,query):
    uq = ['user',user_intent,params,query]
    self.conversation.append(['USER',uq])
    self.model.add_state(uq,'USER')

    
  def generate_output(self):
    # TAOTODO:
    pass




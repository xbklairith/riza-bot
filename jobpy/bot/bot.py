"""
Bot engine
@author Tao PR (github.com/starcolon)
CopyRight 2016-present
"""

import numpy as np
import os.path
import pickle
import json
import uuid
from termcolor import colored

class Bot:
  # Initialise the bot, and having required modules
  # injected in
  # @param {TypeClass} IntentClassifier class
  # @param {TypeClass} TextHasher class
  def __init__(self,IntentClf,TextHash):
    self.IntentClf    = IntentClf
    self.TextHash     = TextHash
    self.kb           = {} # Knowledge base of everything
    self.conversation = []

    # Generate a conversation UUID
    self.uuid         = str(uuid.uuid1())

  """
  Register an intent classifier model
  """
  def add_intent_clf(self,clf):
    self.clf     = clf

    # Make in-built functions for intent classification
    self._intent = self.IntentClf.classify(self.clf)
    self._train  = self.IntentClf.train(self.clf)

  """
  Register a talkflow model
  """
  def add_talk_flow(self,talk):
    self.talkflow = talk

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
    self._hash  = self.TextHash.hash(self.hasher,learn=True)

  """
  Given an input, extract a probable intent with arguments
  """
  def extract_intent(self,phrase):
    vs     = self._hash([phrase])
    intent = self._intent(vs)
    return intent

  """
  Given an input (whitespace delimited), extract the latent knowledge
  attached in the sentence
  """
  def extract_knowledge(self,phrase):
    pass # TAOTODO: Use POS to extract message

  """
  Add a user input (as a state in the conversation model)
  """
  def add_input(self,query):
    # Extract user's intent
    user_intent = extract_intent(query)
    params = None # TAOTODO: Extract params with POS

    uq = ['user',user_intent,params,query]
    # Append the new input to the conversation list
    self.conversation.append(uq)
    # Also register the state (user query) to the conversation model
    self.model.add_state(uq,'USER')
    return uq

  """
  Get the historical sequence of dialogs so far
  @return {List} of intents
  """
  def dialog_sequence(self):
    return [intent for who,intent,params,query in self.conversation]


  """
  Given the current conversation dialog,
  generate the best output (action) which may lead 
  to the desired state (next user's action)
  """
  def generate_output(self):
    # TAOTODO:

    # Check out the most recent state (user's input)
    recent_state = self.conversation[-1]
    u,user_intent,u_params,user_query = recent_state

    # Generate the next preferred state
    # TAOTODO:

    botq = ['bot',bot_intent,params,query]
    self.model.add_transition(user_intent,)
    pass




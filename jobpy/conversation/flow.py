"""
Probabilistic conversation flow
@author Tao PR (github.com/starcolon)
CopyRight 2016-present
"""

import numpy as np
import os.path
import pickle
import json
from termcolor import colored
from hmmlearn import hmm

DIALOG_UNKNOWN     = 0
DIALOG_GREET       = 0x01
DIALOG_QUERY       = 0xA5
DIALOG_INFORM      = 0x42
DIALOG_FAREWELL    = 0xFF

"""
TalkFlow defines how a dialog flows from one to another as a conversation.
This derives Markov chain for its probability-driven to define 
how an intention transitions to one another.
  X : observations   => Intents
  Z : hidden states  => Dialog types (superset of intents)
  A : transitions    => How dialog type transtions to each other
  π : initial probs  => How probable each dialog starts with
"""
class TalkFlow:
  def __init__(self,n_):
    # Initially, create an empty new model
    np.random.seed(100)
    self.model = hmm.GaussianHMM()

  def set_intents(self,intents):
    pass

  def set_dialogs(self,dialogs):
    pass

  """
  Define how a dialog is observed as different intents.
  @param {String} dialog
  @param {List} list of tuples: (intent, probability 0~1)
  """
  def set_observation(self,dialog,intents):
    pass

  def save(self,path):
    pass

  def load(self,path):
    pass
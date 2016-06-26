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
from hmmlearn.hmm import GaussianHMM
from enum import Enum

"""
TalkFlow defines how a dialog flows from one to another as a conversation.
This derives Markov chain for its probability-driven graph to define 
how an intention transitions to one another.
  X : observations   => Intents
  Z : hidden states  => Hidden dialog semantics
  A : transitions    => How dialog type transtions to each other
  π : initial probs  => How probable each dialog starts with
"""
class TalkFlow:
  def __init__(self):
    # Initially, create an empty new model
    np.random.seed(100)
    self.model = None
    self.intents = [] # List of registered intents

    # TAOTODO: Assign a vector of distribution of dialog types

  """
  Register the list of supported intents
  @remark : Order of the tuple in the list DOES MATTER.
  @param {List} list of tuples: (intent, initial probability of 0~1)
  """
  def set_intents(self,intents):
    # Create a new model if not yet
    if self.model is None:
      self.model = GaussianHMM(
        n_components=len(intents),
        convariance_type="diag",
        n_iter=80
      )
    # Initialise starting probabilities of those intents (X)
    self.model.start_prob = np.array([p for intent,p in intents])
    self.intents = [intent for intent,p in intents]

  def save(self,path):
    pass

  def load(self,path):
    pass
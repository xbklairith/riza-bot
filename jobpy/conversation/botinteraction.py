"""
Bot interaction training model
@author Tao PR (github.com/starcolon)
CopyRight 2016-present
"""

import numpy as np
import os.path
import pickle
import json
from termcolor import colored
from .conversationmodel import ConversationModel

class BotInteractionModel(ConversationModel):
  def __init__(self,alpha):
    self.alpha = alpha # Learning rate 0~1
    self.Q = {} # Action policy matrix : State => Action => Q value

  """
  Q-Learning:
  Get the Q value of an action taken on a state.
  """
  def q(self,state,action):
    if state in self.Q and action in self.Q[state]:
      return self.Q[state][action]
    else:
      return 0

  """
  Q-Learning:
  Set the Q value of an action taken on a state.
  """
  def set_q(self,state,action,q):
    if state not in self.Q:
      self.Q[state] = {}
    self.Q[state][action] = q

  """
  Q-Learning:
  Learn a transition from a state => state_ 
  in a situation where the bot takes an action.
  A reward value of the next state will be taken into account.
  """
  def learn_q(self,state,state_,action,reward):
    # List all actions it can take on the next state
    next_actions = self.get_actions(state_)
    # Get the best Q value of the best action
    best_q = 0
    for act in next_actions:
      q      = self.q(state_,act)
      best_q = q if q>best_q else best_q

    q = reward + self.alpha * best_q
    self.set_q(state,action,q)


  """
  Return the best action for a state
  """
  def choose_best_action(self,state):

    def by_q(tup):
      act, q = tup
      return -q

    if state in self.Q:
      actions = [(act,q) for act,q in self.Q[state].items()]
      if len(actions)>0:
        return sorted(actions,by_q)[0]
      else:
        return None
    else:
      return None











"""
Conversation Model (Human-bot interaction)
@author Tao PR (github.com/starcolon)
CopyRight 2016-present
"""

import numpy as np
import os.path
import pickle
import json
from termcolor import colored

class ConversationModel:
  def __init__(self):
    self.states = set() # User's input
    self.actions = set() # Bot's response
    self.transitions = {} # Map: state => action => (state_, confidence)

  def save(self,path):
    with open(path,'wb+') as f:
      pickle.dump(self,f)

  @staticmethod
  def load(path):
    with open(path,'rb') as f:
      return pickle.load(f)

  def add_state(self,state,state_type):
    self.states.add((state_type, state))
    if state not in self.transitions:
      self.transitions[state] = {}

  def add_action(self,action):
    self.actions.add(action)

  def add_transition(self,state,state_,action,confidence):
    # Check whether the action which maps from
    # state -> state_ 
    # already exists?
    self.add_state(state)
    self.add_state(state_)
    self.add_action(action)
    if action not in self.transitions[state]:
      self.transitions[state][action] = []

    self.transitions[state][action].append((state_,confidence))

  """
  List all available actions and their possible transitions
  given the current state
  @return {Dict} which maps action => [(next_state,confidence)]
  """
  def get_transitions(self,state):
    return self.transitions[state]

  """
  List all actions which the bot can take on a state
  @return {List} of actions
  """
  def get_actions(self,state):
    return self.transitions[state].keys()

  """
  List all next states if we apply an action on the current state.
  The result is a tuple of next state and its confidence score.
  @return {List} of tuple (next_state, confidence), ordered by confidence value
  """
  def next_states(self,state,action):
    def most_confident_first(n):
      s,c = n
      return -c

    if action in self.transitions[state]:
      return sorted(self.transitions[state][action], most_confident_first)
    else:
      return []



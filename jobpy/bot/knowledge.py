"""
Knowledge graph structure of a bot
"""

import pickle
import json

class BotKnowledge:
  
  def __init__(self):
    self.__kb = {}

  """
  Recall a linked story from the memory
  """
  def recall(self,keywords):
    pass

  """
  Store a new linked story in the memory
  """
  def store(self,keywords):
    pass

  """
  Reconstruct and refresh the entire knowledge graph
  """
  def rehabilitate(self):
    pass

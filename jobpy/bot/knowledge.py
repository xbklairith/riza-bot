"""
Knowledge graph structure of a bot
"""

import pickle
import json
import pyorient

class BotKnowledge:
  
  def __init__(self,dbname,usrname,psw):
    # Initialise a connection to OrientDB
    self.__kb      = pyorient.OrientDB('localhost',2424)
    self.__session = self.__kb.connect(usrname,psw)
    if self.__kb.db_exists(dbname,pyorient.DB_TYPE_GRAPH)
      self.__kb.db_open(dbname,usrname,psw)
    else 
      self.__kb.db_create(dbname,pyorient.DB_TYPE_GRAPH)
      self.__kb.db_open(dbname,usrname,psw)

  def end(self):
    self.__kb.db_close()

  """
  Recall a linked story from the memory
  """
  def recall(self,topic,link):
    #TAOTODO:
    pass

  """
  Store a new linked story in the memory
  """
  def store(self,topic,link,topic_):
    pass

  """
  Reconstruct and refresh the entire knowledge graph
  """
  def rehabilitate(self):
    pass

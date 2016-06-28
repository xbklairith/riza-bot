"""
Conversation data storage module
@author Tao PR (github.com/starcolon)
CopyRight 2016-present
"""

import datetime
from pymongo import MongoClient
from pymongo import InsertOne

COLLECTION_CONVERSATION   = "conversation"

class Conversation:

  def __init__(self,host,db):
    server           = "mongodb://{0}:27017/".format(host)
    self.connector   = MongoClient(server)
    self._db         = self.connector[db]
    self._collection = self._db[COLLECTION_CONVERSATION]
    print("Connected to conversation collection at: {0}".format(server))

  def add(self,uid,entry):
    insert = InsertOne(entry)
    self._collection.bulk_write([insert])

  def find(self,conditions):
    return self._collection.find(conditions)


"""
A class which represents a single phrase or sentence 
as a dialog spoken by a person in the conversation.
"""
class DialogEntry:

  def __init__(self,speaker,phrase,intent,params):
    self.speaker = speaker
    self.phrase  = phrase
    self.intent  = intent
    self.params  = params
    self.t       = datetime.datetime.utcnow()

  """
  Add a new dialog entry to the specified conversation data source
  @param {String} Unique identifier of a conversation
  @param {Conversation} data source object
  """
  def add_to(self,uid,conv):
    conv.add(uid,{
      'conversation': uid,
      't':            self.t,
      'user':         self.speaker,
      'phrase':       self.phrase,
      'intent':       self.intent,
      'params':       self.params
    })

"""
User query data storage module
@author Tao PR (github.com/starcolon)
CopyRight 2016-present
"""

from pymongo import MongoClient
from pymongo import InsertOne

"""
User query data storage interface
"""

COLLECTION_QUERY_TEXT   = "query"

class UserQuery:
  def __init__(self,host,db):
    server           = "mongodb://{0}:27017/".format(host)
    self.connector   = MongoClient(server)
    self._db         = self.connector[db]
    self._collection = self._db[COLLECTION_QUERY_TEXT]
    print("Connected to query collection at: {0}".format(server))

  """
  Add a new user query entry to the data storage
  """
  def add(self,entry):
    insert = InsertOne(entry)
    self._collection.bulk_write([insert])

  def find(self,conditions={}):
    return self._collection.find(conditions)

"""
Query entry which represents each record in
the database
"""
class UserQueryEntry:
  def __init__(self,user,rawquery,intent,params):
    self.user        = user
    self.rawquery    = rawquery
    self.intent      = intent
    self.params      = params
  
  def add_to(self,userquery):
    userquery.add({
      'user':   self.user,
      'query':  self.rawquery,
      'intent': self.intent,
      'params': self.params
    })

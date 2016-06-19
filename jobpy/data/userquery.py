"""
User query data storage module
@author Tao PR (github.com/starcolon)
CopyRight 2016-present
"""

"""
User query data storage interface
"""
class UserQuery:
  def __init__(self,host,dbcache):
    # TAOTODO:
    pass

  """
  Add a new user query entry to the data storage
  """
  def add(entry):
    pass

"""
Query entry which represents each record in
the database
"""
class UserQueryEntry:
  def __init__(self,user,rawquery,vectorquery,intent,params):
    self.user        = user
    self.rawquery    = vectorquery
    self.vectorquery = vectorquery
    self.intent      = intent
    self.params      = params
  
  def add_to(self,userquery):
    userquery.add(self)

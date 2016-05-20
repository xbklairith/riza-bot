"""
String tokeniser operation
@author Tao PR (github.com/starcolon)
CopyRight 2016-present
"""

from tornado import httpclient
from termcolor import colored
import json

tokeniser_serv = 'http://localhost:9861/break/'

# @input: String
# @output: list of string
def tokenise(phrase):
  # Do not proceed with empty input
  if phrase is None: return []
  if len(phrase)==0: return []

  # Generate a tokenising request
  return __request(phrase)

# Make a request to the tokeniser service
def __request(input0):
  client = httpclient.HTTPClient()
  output = None
  try:
    print(colored('tokenising.. ','yellow') + input0)
    req    = httpclient.HTTPRequest(tokeniser_serv,method='POST',body=input0)
    resp   = client.fetch(req)
    output = resp.body

    # Decode bytes
    output = output.decode('utf-8')
    # Parse the JSON response to a hash object
    output = json.loads(output)

  except httpclient.HTTPError as e:
    # HTTP error header
    print(colored('HTTP Error : ' + str(e),'red'))
  except Exception as e:
    # Some unhandled error
    print(colored('ERROR : ' + str(e), 'red'))

  client.close()

  print(colored('{Tokeniser received:}','white'))
  print(colored(output,'white'))

  return output
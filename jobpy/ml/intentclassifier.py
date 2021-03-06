"""
Vector space classifier
@author Tao PR (github.com/starcolon)
CopyRight 2016-present
"""
import numpy as np
import os.path
import pickle
import json
from termcolor import colored
from sklearn.cluster import KMeans

def new(n_labels=10,method='kmeans'):
  methods = {
    'kmeans': KMeans(
      n_clusters = n_labels
    )
  }
  return methods[method]

def save(operations,path):
  with open(path,'wb+') as f:
    pickle.dump(operations,f)

def load(path):
  with open(path,'rb') as f:
    return pickle.load(f)

def safe_load(path):
  if os.path.isfile(path): 
    print(colored('Intent classifier loaded.','cyan'))
    return load(path)
  else: 
    print(colored('Intent classifier created...','yellow'))
    return new()

# Classify multiple vectors at a time using 
# the specified trained operations
def classify(opr):
  def classify_us(vectors):
    return opr.transform(vectors)
  return classify_us

def train(opr):
  def fit(vectors,labels):
    return opr.fit(labels,vectors)
  return fit

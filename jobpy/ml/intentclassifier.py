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

def new(n_labels=10):
  kmeans = KMeans(
    n_clusters = n_labels
  )
  return kmeans


def save(operations,path):
  with open(path,'wb+') as f:
    pickle.dump(operations,f)

def load(path):
  with open(path,'rb') as f:
    return pickle.load(f)

def safe_load(path):
  if os.path.isfile(path): return load(path)
  else: return new()

# Classify multiple vectors at a time using 
# the specified trained operations
def classify(opr):
  def classify_us(vectors):
    return opr.transform(vectors)
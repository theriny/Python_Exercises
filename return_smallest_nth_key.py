# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 23:43:21 2022

@author: theri
"""
import math
'''
Example Input Data

inputDict =  {"a": 10,"b": 20,"c": 3,"d": 2,"e": 9}
n = 1 
'''


def return_smallest_key(inputDict, n):
  
  
  
  
  # extract keys from input dictionary
  lstKeys = list(inputDict.keys())
  
  # sort keys from input dictionary
  #lstKeys.sort()

  # extract values from input dictionary
  lstValues = list(inputDict.values())
  
  if n > len(lstValues):
    return (None)
  
  elif n == 0:
    return (None)
  
  else:

    n = n-1
    
    # create empty set to store values once they've been seen
    seen = set()

    # create empty list to store duplicate values from input dictionary
    dupes = []

    # find duplicate values
    for value in lstValues:
        if value in seen:
            dupes.append(value)
        else:
            seen.add(value)



    value_lst = [] # to store dict values
    key_lst = [] # to store duplicate keys

    for key in lstKeys:
      result = inputDict[key]
      if result in dupes:
        key_lst.append(key)
        value_lst.append(result)
      else:
        value_lst.append(result)

    #sort value_lst and key_lst
    value_lst.sort()
    key_lst.sort()

    #find the nth value
    nth_value = value_lst[n] #nth value is a number but we don't know what the key is

    #create new dict that swaps value and keys from input dict
    new_dict = {}

    for i in range(len(lstKeys)):
      new_dict.update({lstValues[i]:lstKeys[i]})

    #find key that corresponds to nth value
    nkey = new_dict[nth_value]

    if nkey not in key_lst:
      answer = nkey
    else:
      answer = key_lst[0]
    
    return(answer)

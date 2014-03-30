import sys
from copy import deepcopy

dictionary_in = ['star','stat','sat','at','a']
existing_list = []


def find_subword(word_in, existing_list, dictionary_in):
  word_subset = []
  for i in range(len(word_in)):
    word_subset.append(str(word_in[:i] + word_in[i+1:]))
 
  for i in word_subset:
    if i in dictionary_in:
      existing_list.append(i)
      find_subword(i,existing_list,dictionary_in)
 
  return existing_list

find_subword('start',existing_list,dictionary_in)
print(existing_list)

import sys
from copy import deepcopy

dictionary_in = ['star','stat','sat','at','a']
existing_list = []


def find_subword(start_word, existing_list, dictionary_in):
  word_subset = []
  start_word
  for i in range(len(start_word)):
    word_subset.append(str(start_word[:i] + start_word[i+1:]))
 
  for i in word_subset:
    if i in dictionary_in:
      if (find_subword(i,existing_list,dictionary_in) is not None or len(i) == 1):
         existing_list.append(i)
         return existing_list
 
  return None

index = int(0)
  
find_subword('start',existing_list,dictionary_in)
print(existing_list)

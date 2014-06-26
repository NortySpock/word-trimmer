import sys
from copy import deepcopy

my_dictionary = set()
word_subset = []
found_smaller_word = 0
smaller_word = ''

list_of_subwords = []
niners = []

f = open('this_dictionary.txt', 'r')
for line in f:
  strip_line = line.strip()
  if strip_line == strip_line.lower() and strip_line.isalpha():
    my_dictionary.add(strip_line)
    if len(strip_line) >= 9:
      niners.append(strip_line)
f.close()


def find_subword(word_in, existing_list, dictionary_in):
  word_subset = []
  for i in range(len(word_in)):
    word_subset.append(str(current_word[:i] + current_word[i+1:]))
  

for nine in niners:
  starting_word = nine
  current_word = deepcopy(starting_word)
  full_word_list = []
  full_word_list.append(starting_word)
  done = False
  while not done:
    for i in range(len(current_word)):
      word_subset.append(str(current_word[:i] + current_word[i+1:]))

    found_smaller_word = 0
    for i in word_subset: 
      if i in my_dictionary:
        found_smaller_word = 1
        smaller_word = str(i)
        full_word_list.append(smaller_word)
        break
      if found_smaller_word:
        break
          
    word_subset = []
    if found_smaller_word:
      current_word = deepcopy(smaller_word)
    elif len(current_word) <= 1:
      print("Success! length:"+str(len(starting_word)))
      for word in full_word_list:
        print(word)
      print("-")
      done = True
    else:
      done = True


import sys
from copy import deepcopy

my_dictionary = set()
word_subset = []
found_smaller_word = 0
smaller_word = ''

list_of_subwords = []
niners = []

f = open('dictionary.txt', 'r')
for line in f:
  strip_line = line.strip().lower()
  if len(strip_line) < 1:
    pass #don't add
  elif len(strip_line) == 1:
    if strip_line in('a','i','o'):
      my_dictionary.add(strip_line)
  else:
    my_dictionary.add(strip_line)

  if len(strip_line) >= 9:
    niners.append(strip_line)
f.close()



#outfile = open('output.txt', 'w')


# def find_awesome_word():

def find_subword(word_in, existing_list, dictionary_in):
  word_subset = []
  for i in range(len(word_in)):
    word_subset.append(str(current_word[:i] + current_word[i+1:]))
  

for nine in niners:
  starting_word = nine
  current_word = deepcopy(starting_word)
  print "-"
  done = False
  while not done:
    for i in range(len(current_word)):
      word_subset.append(str(current_word[:i] + current_word[i+1:]))

      
      
    found_smaller_word = 0
    for i in word_subset: 
      if i in my_dictionary:
        print('found smaller word: ' + i)
        found_smaller_word = 1
        smaller_word = str(i)
        list_of_subwords.append(smaller_word)
        break
      if found_smaller_word:
        break
          
    word_subset = []
    if found_smaller_word:
      current_word = deepcopy(smaller_word)
    elif len(current_word) <= 1:
      print("Success! " + current_word)
      
      #outfile.write()    
      done = True
    else:
      print("Failed:"+current_word)
      list_of_subwords = []
      done = True

#outfile.close()

#input("waiting for input to close...")

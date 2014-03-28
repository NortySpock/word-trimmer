import sys
from copy import deepcopy

master_word_list = []
my_dictionary = []
word_subset = []
found_smaller_word = 0
smaller_word = ''

list_of_subwords = []

f = open('9words.txt', 'r')
for line in f:
  master_word_list.append(line.strip())
f.close()

f = open('8_chars_or_less.txt','r')
for line in f:
  my_dictionary.append(line)

starting_word = "startling"
current_word = deepcopy(starting_word)

outfile = open('list_of_9_char_words_and_subwords.txt', 'w')


# def find_awesome_word():

# def find_subword():
  



while 1:
  for i in range(len(current_word)):
    word_subset.append(str(current_word[:i] + current_word[i+1:]))

    
    
  found_smaller_word = 0
  for i in word_subset: 
    for j in master_word_list:
      if str(i) == str(j):
        print('FOUND_SMALLER_WORD!')
        found_smaller_word = 1
        smaller_word = str(i)
        list_of_subwords.append(smaller_word)
        break
    if found_smaller_word:
      break
        
  word_subset.clear()
  if found_smaller_word:
    current_word = deepcopy(smaller_word)
  elif len(current_word) <= 1:
    print("Success! " + current_word)
    outfile.write()
    break
  else:
    print("Failed:"+current_word)
    list_of_subwords.clear()
    break

outfile.close()

input("waiting for input to  close...")

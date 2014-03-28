import sys
from copy import deepcopy
import string

master_word_list = []
word_subset = []
done = 0
found_smaller_word = 0
smaller_word = ''

f = open('dictionary.txt', 'r')
for line in f:
   master_word_list.append(line.strip())
f.close()

print(master_word_list)

starting_word = "startling"
current_word = deepcopy(starting_word)

while not done:
   for i in range(len(current_word)):
      word_subset.append(str(current_word[:i] + current_word[i+1:]))

      
      
   found_smaller_word = 0
   for i in word_subset:
      print ("i:"+i+":")     
      for j in master_word_list:
         print ("j:"+j+":")
         if str(i) == str(j):
            print('FOUND_SMALLER_WORD!')
            found_smaller_word = 1
            smaller_word = str(i)
            print(smaller_word)
            break
      if found_smaller_word:
         break
         
   word_subset.clear()
   if found_smaller_word:
      print("subword:"+smaller_word)
      current_word = deepcopy(smaller_word)
      print ("my_current_word:"+current_word+":")
   elif len(current_word) <= 1:
      print("Success.")
      break
   else:
      print("Failed:"+current_word)
      print("FAILURE!")
      break


input("waiting for input to  close...")

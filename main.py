import sys
from copy import deepcopy

master_word_list = []
word_subset = []
done = False
found_smaller_word = False
smaller_word = ''

f = open('dictionary.txt', 'r')
for line in f:
   master_word_list.append(line)
f.close()

print(master_word_list)

starting_word = "startling"
current_word = deepcopy(starting_word)

while not done:
   for i in range(len(current_word)):
      word_subset.append(str(starting_word[:i] + starting_word[i+1:]))

      
      
   found_smaller_word = False
   for i in word_subset:
      print ("i:"+i)     
      for j in master_word_list:
         print ("j:"+j)
         if i == j:
            found_smaller_word = True
            smaller_word = i
            print(smaller_word)
            break
      if found_smaller_word:
         break
         
   word_subset.clear()
   if found_smaller_word:
      print("subword:"+smaller_word)
   elif len(current_word) <= 1:
      done = True
      print("Success.")
   else:
      done = True
      current_word = smaller_word
      print("FAILURE!")


input("waiting for input to  close...")

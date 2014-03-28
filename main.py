import sys

master_word_list = []
word_subset = []

f = open('dictionary.txt', 'r')
for line in f:
   master_word_list.append(line)
f.close()

starting_word = "startling"

for i in range(len(starting_word)):
   # print ("start half:", starting_word[:i])
   # print ("i         :", starting_word[i]
   # print ("end   half:", starting_word[i:])
   print (str(starting_word[:i] + starting_word[i+1:]))
   # word_subset.append(str(starting_word[:i] + starting_word[i:]))

input("waiting for input to  close...")


import sys
import os

master_word_list = []

f = open('dictionary.txt', 'r')
for line in f:
   master_word_list.append(line.strip())
f.close()


out = open("8_chars_or_less.txt",'w')
for i in master_word_list:
   if len(i) < 9:
      out.write(i + '\n')
f.close()

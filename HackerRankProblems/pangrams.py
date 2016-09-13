import sys

string = raw_input().strip()

alphabets = {}
pangram = False
for i in string:
  if i.isalpha() and i.lower() not in alphabets and not i.isdigit():
    alphabets[i.lower()] = 1
    if len(alphabets) >= 26:
      print "pangram"
      pangram = True
      print alphabets
      break 

if not pangram:
  print "not pangram"


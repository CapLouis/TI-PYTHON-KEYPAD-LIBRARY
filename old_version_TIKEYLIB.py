from sys import *
from time import *

def chrput(c=0):
  l=True
  i=138
  stdout.write(" ")
  while l:
    stdout.write("\b"+chr(i)+chr(131)+"\b")
    g=getkey()
    if g==" [A":
      if i<255:
        i+=1
      if i==143:
        i=162
    elif g==" [B":
      if i>=34:
        i-=1
      if i==161:
        i=142
    elif g==" [C":
      l=False
  if c==0:
    stdout.write("\n")
    return chr(i)
  else:
    return i

def demo(tn=1):
  t=monotonic()
  l=""
  while (t+tn)>monotonic():
    l+=getkey()
  print(len(l)/3,"touches appuyees en ",tn,"secondes")
  return l

def keyput(l):
  s=""
  c=""
  for i in range(l):
    c=getkey(1)
    if c!="\b":
      s+=c
      stdout.write(s[i])
    else:
      s+=chr(ch(1))
      stdout.write(s[i]+"\b")
  stdout.write("\n")
  return s

def getkey(n=0):
  if n==0:
    return stdin.read(3).replace(chr(27)," ")
  else:
    return stdin.read(1)

def ispressed(key="up",keylist=[]):
  if key=="enter":
    key=" [F"
  if key=="up":
    key=" [A"
  if key=="down":
    key=" [B"
  if key=="right":
    key=" [C"
  if key=="left":
    key=" [D"
  if key=="annul":
    key=" [2"

  if key==keylist:
    return True
  else:
    return False

"""use like this :
g=getkey()
if ispressed("up",g): #if up key is pressed
  #do if pressed




"""

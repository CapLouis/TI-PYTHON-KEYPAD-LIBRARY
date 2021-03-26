from sys import stdin,stdout

def getkey():
  s=stdin.read(1)
  if s==chr(27):
    s=stdin.read(2) 
    if s=="[2":
      stdin.read(1)
  return s

def ispressed(key,gotkey):
  if key=="up":
    key="[A"
  if key=="down":
    key="[B"
  if key=="left":
    key="[D"
  if key=="right":
    key="[C"
  if key=="enter":
    key="[F"
  if key=="annul":
    key="[2"
  if key=="del":
    key="\b"
  if key==gotkey:
    return True
  else:
    return False

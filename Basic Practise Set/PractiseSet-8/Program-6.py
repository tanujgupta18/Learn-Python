def rem(l,word):
  for item in l:
    l.remove(word)
    return l

l = ["Rohan","Rani","Mali"]

print(rem(l,"Mali"))
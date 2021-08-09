import sys

def sum():
  x= str(input("Number: " ))
  temp=0
  for i in x:
    if i.isnumeric():
      temp = temp + int(i)
    else:
      continue
  return(temp)

def file_sum(file):
  with open(file, "r") as f:
    for readline in f:
      x=readline
      temp=0
      for i in x:
        if i.isnumeric():
          temp = temp + int(i)
        else:
          continue
      return(temp)

def hexnumbers():
  valid_values= ('A','B','C','D','E','F','a','b','c','d','e','f','0','1','2','3','4','5','6','7','8','9')
  x= str(input("Number: " ))
  temp=0
  for i in x:
    if i not in valid_values:
      print('invalid numbers')
      break
    y = int(i, 16)
    temp = temp + int(i, 16)
  return(temp)

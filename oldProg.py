#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
import sys

def sum():
  x= str(input("Enter the number: " ))
  temp=0
  for i in x:
    if i.isnumeric():
      temp = temp + int(i)
    else:
      continue
  print(temp)

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
      print(temp)
def numbers(x):
  temp=0
  for i in x:
    y = int(i, 16)
    temp = temp + int(i, 16)
  print(temp)
  

condition=""
if (len(sys.argv) == 1):
  condition = ""
else:
  condition = sys.argv[1]

if (condition == "-x"):
  x = str(input("Enter the number: "))
  numbers(x)
elif (condition == "-f"):
  file_sum(sys.argv[2])
elif (condition == ""):
  sum()
else:
  print("No arguments or options are considered") 

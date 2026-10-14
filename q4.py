# Convert a tuple into a list, modify it, and convert it back into a tuple.
l=[]
cl=[]
def start():
  r=int(input("Enter range : "))
  for i in range(r):
    e=int(input("Enter element : "))
    l.append(e)
  t=tuple(l)
  print(t)

def transform():
  cl=list(l)
  print(cl)

def modify():
  ind=int(input("Enter the index where you want to modify : "))
  mod=int(input("Enter modification number : "))
  l[ind]=mod
  print(l)

  
def repeat():
  while True : 
    ask=int(input("\nEnter 1 to modify the tuple \nEnter 2 to change \nEnter 3 to Exit \n:>> "))
    if ask == 1:
      modify()
    elif ask == 2:
      transform()
    elif ask == 3:
      break
    else: 
      print(f"You are not following the command : ")

start()
repeat()

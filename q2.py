# Find the largest and smallest element in a tuple.

l=[]
r=int(input("Enter range : "))
for i in range(r):
  e=int(input("Enter elements : "))
  l.append(e)
t=tuple(l)

s=t[0]
g=t[0]
for num in t:
  if num < s : 
    s=num
  elif num > s:
    g=num
print(f"The smallest number of the tuple is : {s}\nThe greatest number of the tuple is : {g}")

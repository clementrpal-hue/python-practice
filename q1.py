# Create a tuple containing 10 numbers and calculate its sum without using sum()

l=[]
r=int(input("Enter range of tuple : "))
for i in range(r):
  e=int(input("Enter element in the tuple : "))
  l.append(e)
t=tuple(l)
c=0
for i in range(0,len(l)-1,1):
  for num in t:
    c=c+num
print(c)
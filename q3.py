# Count how many times a particular number occurs in a tuple

l=[]
r=int(input("Enter range : "))
for i in range(r):
  e=int(input("Enter element : "))
  l.append(e)
t=tuple(l)

print(t)
s=int(input("\nEnter the number you want to search from this : "))
c=0
for num in t:
  if num == s:
    c+=1
print(f"The number {s} occured {c} times")

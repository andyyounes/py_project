import random
x=int(input("Enter the length of the array: "))
s=[]
for i in range (x):
    s.append(random.randint(1,20))
print(s)
n=max(s)
m=min(s)
print("max= ",n)
print("min= ",m)
sumi=0
p=1
for i in range (x):
    sumi+=s[i]
    p*=s[i]
print("Sum of all int in array is: ",sumi)
print("Product of all int in array is: ",p)

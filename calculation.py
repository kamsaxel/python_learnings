print("3. Sum of the numbers = ",sum(numbers))
sums=sum(numbers)
count=len(numbers)
average=sums//count
print("4. Average of the numbers = ",average)
print("5. Second maximun number = ",)
a=[]
for i in numbers:
    if i%2==0:
        a.append(i)
print("6. Odd numbers =",str(a).replace("[","").replace("]",""))
b=[]
for i in numbers:
    if i%2==1:
        b.append(i)
print("7. Even numbers =",str(b).replace("[","").replace("]",""))
c=[]
for i in numbers:
    if 10 <= i <= 99:
        c.append(i)
print("8. Two digit numbers =",str(c).replace("[","").replace("]",""))
d=[]
for i in numbers:
      if i<0:
          d.append(i)
print("9. Negative numbers = ",str(d).replace("[","").replace("]",""))
e=[]
for i in numbers:
      if i>0:
          e.append(i)
print("10. Positive numbers = ",str(e).replace("[","").replace("]",""))
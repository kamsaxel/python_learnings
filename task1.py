##a = int(input())
##if a%2 == 0:
##    print(chr(a * 2 % 26 + 64))
##elif a%2 == 1:
##    print(chr(64+((number+2)*2)%26))
##else:
##    print("Invalid input")
a=input("Enter the word:")
l=len(a)
if l%2 == 0:
    t = l//2
    for i in range(1,l+1):
        print(i*t)
else:
    for i in range(1,l+1):
        print(i*l)


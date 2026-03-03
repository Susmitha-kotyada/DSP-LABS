#CONDITIONS
#1 Marks and Grades
'''
m=int(input("enter marks:"))
if(m>=90):
    print("your grade is Ex")
elif(m>=80):
    print("your grade is A")
elif(m>=70):
    print("your grade is B")
elif(m>=60):
    print(" your grade is C")
elif(m>=50):
    print("your grade is D")
elif(m>=40):
    print(" your grade is E")
else:
    print("You are failed")

'''
#2 leap year
'''
y=int(input("enter year:"))
if(y%4==0 and (y%100!=0 or y%400==0)):
    print(y,"is a leap year")
else:
    print(y,'is not a leap year')
'''

#BRANCHING

#1 RAILWAY TICKET FARE SYSTEM
'''
age=int(input("enter your age:"))
fare=0
if age<=5:
    print("you dont need to take ticket")
else:
    class_type=input("enter type of the class:")
    distance=int(input("enter distance:"))
    if class_type=='general' or class_type=='g':
        fare=distance/3
        print("fare is",fare)
    elif class_type=='second' or class_type=='s':
        fare=distance/2
        print("fare is",fare)
    elif class_type=='ac':
        fare=distance
        print("fare is",fare)
    else:
        print("enter correct class")
'''
#2 ELECTRICITY BILL SYSTEM

#LOOPS
#1 even numbers
'''
n=int(input("enter n:"))
print("even numbers:")
for i in range(1,n,1):
    if i%2==0:
        print(i,end=' ')
 '''  
#2 reverse number
'''
n=int(input("enter a number:"))
rev=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print("reverse of the number:",rev)
'''
#3 fibonacci series
'''
n=int(input("enter range of series:"))
a=0
b=1
print("Fibonacci series:")
print(a,b,end=' ')
for i in range(1,n-2,1):
    c=a+b
    print(c,end=' ')
    a=b
    b=c
'''

#4 Factorial of a number
'''
f=int(input("enter number:"))
fact=1
for i in range(1,f+1,1):
    fact=fact*i
print("Factorial of",f,"is",fact)
'''

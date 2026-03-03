

#1
print("VAISHIKA")
print("CSE")'''

#2 Arithmetic operations
a=23
b=11
print(a,"+",b,"=",a+b)
print(a,'-',b,'=',a-b)
print(a,'*',b,'=',a*b)
print(a,'/',b,'=',a/b)

#3 even or odd
print(a,'%',b,'=',a%b)
c=int(input("enter a number: "))
if(c%2==0):
    print(c,'is an even number')
else:
    print(c,'is an odd number')

#4 largest among 5 numbers
print("enter 5 numbers:")
a1=int(input("enter 1st number:"))
a2=int(input("enter 2nd number:"))
a3=int(input("enter 3rd number:"))
a4=int(input("enter 4th number:"))
a5=int(input("enter 5th number:"))
if(a1>a2 and a1>a3 and a1>a4 and a1>a5):
    print(a1,'is the largest number')
elif(a2>a1 and a2>a3 and a2>a4 and a2>a5):
    print(a2,'is the largest number')
elif(a3>a1 and a3>a2 and a3>a4 and a3>a5):
    print(a3,'is the largest number')
elif(a4>a1 and a4>a2 and a4>a3 and a4>a5):
    print(a4,'is the largest number')
else:
    print(a5,'is the largest number')

#5  degree celsius to fahrenheit
ce=int(input("enter celsius: "))
f=(ce*(9/5))+32
print(ce,'in fahrenheit is',f)

#6 positive or negative or zero
p=int(input("enter number:"))
if(p>0):
    print(p,'is a positive number')
elif(p<0):
    print(p,'is a negative number')
else:
    print(p,'is a zero')

#7 multiplication table
m=float(input('enter number:'))
r=int(input("enter range:"))
for i in range(1,r+1,1):
    print(m,'*',i,'=',m*i)

#8 sum of n natural numbers
range=int(input("enter range of numbers:"))
summ=(range*(range+1))/2
print('total:',summ)


#9 prime number or not
p=int(input("enter number:"))
d=0
for i in range(1,p,1):
    if(p%i==0):
        d=d+1
if(d==1):
    print(p,'is a prime')
else:
    print(p,'is a composite')


#10 no of characters in a string
s=input("enter string:")
l=len(s)
print('no of characters in given string','"',s,'"',':',l)


#11 palindrome
s=input("enter a string:")
st=''
for i in range(len(s)-1,-1,-1):
    st=st+s[i]
if(st==s):
    print(s,'is a palindrome')
else:
    print(s,'is not a palindrome')


#12 vowels and consonants in a string
s=input("enter a string:")
v=['a','e','i','o','u']
v_count=0
c_count=0
for i in s:
    if i in v:
        
        v_count+=1
    else:
        c_count+=1
print('vowels:',v_count,'consonants:',c_count)


#13 uppercase and lowercase letters in a string
st=input("enter a string:")
u,l=0,0
for i in st:
    if i.isupper():
        u+=1
    else:
        l+=1
print('UPPERCASE:',u,'LOWERCASE',l)


#14 largest and smallest in a list
n=int(input("enter no of elements in a list:"))
l=[]
for i in range(1,n+1):
    x=int(input("enter value:"))
    l.append(x)
print(l)
lar=l[0]
small=l[0]
for i in l:
    if i>lar:
        lar=i
for j in l:
    if j<small:
        small=j
print('largest:',lar)
print('smallest:',small)


#15 sum and average of the list
n=int(input("enter no of elements in a list:"))
l=[]
summ=0
for i in range(1,n+1):
    x=int(input("enter value:"))
    l.append(x)
print(l)
for i in l:
    summ+=i
print('sum of numbers:',summ)
avg=summ/n
print('average of numbers:',avg)
'''



#LISTS

#1 Create list
'''
l=[]
n=int(input("enter no of elements in list:"))
for i in range(0,n,1):
    a=int(input("enter number:"))
    l.append(a)
print(l)
'''

#2 largest and smallest in a list
'''
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
'''

#3 sum and average of the list
'''
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

#4 EVEN AND ODD NUMBERS
'''
l=[]
n=int(input("enter no of elements in list:"))
for i in range(0,n,1):
    a=int(input("enter number:"))
    l.append(a)
print(l)
e=0
o=0
for i in l:
    if(i%2==0):
        e+=1
    else:
        o+=1
print("even:",e)
print("odd:",o)
'''

#5 search for an element
'''
l=[]
n=int(input("enter no of elements in list:"))
for i in range(0,n,1):
    a=int(input("enter number:"))
    l.append(a)
print(l)
flag=False
s=int(input("enter search number:"))
for i in range(0,len(l)):
    if l[i]==s:
        flag=True
        break
if flag:
    print(s,'is found at',i)
else:
    print(s,'is not found')
'''

#6 remove an element in the list
'''
l=[11,23,10,5,22]
l.remove(22)
print(l)
'''

#7 reverse the list
'''
l=[11,23,10,5,22]
rev=[]
for i in range(len(l)-1,-1,-1):
    rev.append(l[i])
print("reverse of the list:",rev)
'''

#8 sorting the list
'''
#Ascending order
def sort(l):
    n=len(l)
    for i in range(n):
        for j in range(0,n-i-1):
            if(l[j]>l[j+1]):
                l[j],l[j+1]=l[j+1],l[j]
    return l

l=[11,23,10,5,22]
#l.sort()
print("list:",l)
print("ascending order:",sort(l))

#Descending order
def sort(l):
    n=len(l)
    for i in range(n):
        for j in range(0,n-i-1):
            if(l[j]<l[j+1]):
                l[j],l[j+1]=l[j+1],l[j]
    return l

l=[11,23,10,5,22]
l.sort(reverse=True)
print("descending order:",sort(l))
'''

#9 copy one list into another list
'''
l=[11,23,10,5,22]
lis=[]
lis=l.copy()
print(lis)
'''

#TUPLES
#1 Create tuple
'''
t=()
n=int(input("enter range:"))
for i in range(0,n,1):
    a=int(input("enter element:"))
    t=t+(a,)
print(t)
'''
#2 Acesssing elements in a tuple
'''
t=(11,23,5,10,22)
print(t[2])
print(t[1:4])
print(t[::2])
print(t[-2])
print(t[-1::-1])
'''
#3 count elements in tuple
'''
t=(11,23,5,10,22)
c=0
for i in t:
    c+=1
print("count:",c)
'''
#4 max and min in tuple
'''
t=(11,23,10,5,25)
maxx=t[0]
minn=t[0]
for i in t:
    if(i>maxx):
        maxx=i
print("maximum in the tuple is",maxx)
for i in t:
    if(i<minn):
        minn=i
print("minimum in the tuple is",minn)
'''
#5 tuple to list and list to tuple conversion
'''
t=(11,23,5,10,22)
l=list(t)
print(l)
tt=tuple(l)
print(tt)
for i in tt:
    l.append(i)
print(l)
for i in l:
    tt=tt+(i,)
print(tt)
'''
#6 element exist or not
'''
t=(11,23,5,10,22)
flag=False
s=int(input("enter search number:"))
for i in range(0,len(t)):
    if t[i]==s:
        flag=True
        break
if flag:
    print(s,'is found at',i)
else:
    print(s,'is not found')
'''
#7 index of an element
'''
t=(11,23,5,10,22)
i=t.index(5)
print(i)
'''
#8 tuple with one element
'''
t=()
a=int(input("enter element:"))
t=tuple([a])  #t=t+(a,)
print(t)
'''
#9 Nested tuples
'''
t=(11,23,5,10,22)
t1=(18,17,12,25,15)
t1=((t),)+t1
print(t1)

'''



#DICTIONARY
#1 dict of student details
'''
d={}
n=int(input("enter n:"))
for i in range(1,n+1,1):
    r=int(input("enter roll no:"))
    Id=int(input("enter id:"))
    name=input("enter nsme:")
    d[r]=(Id,name)
print(d)
#2 Acessing values using keys
print(d[2])
'''
#3 adding new key value pair
'''
d={'a':'apple','b':'banana','c':'carrot'}
d['g']='guava'
print(d)
'''
#4 updating value of an existing key
'''
d={1:'amma',2:'nanna',3:'annayya',4:'nenu'}
d[4]='thammuduuu'
print(d)
'''

#5 delete a key from the dictionary
'''
d={'a':'apple','b':'banana','c':'carrot','g':'grapes'}
del d['g']
print(d)
'''





#SETS
#1 create set
'''
s=set()
n=int(input("enter n:"))
for i in range(n):
    a=int(input("enter element:"))
    s.add(a)
#s=set(l)
print(s)
'''
#2 add and remove elements from the set
'''
s={'apple','banana','guava','custard apple','carrot'}
s.add('grapes')
print("set:",s)
s.remove('carrot')
print('updated set:',s)
'''
#3 remove duplicates
'''
s={'html','css','python','css','java','c++'}
d=set()
for i in s:
    if i not in d:
        d.add(i)
print(d)
'''
#4 length of a set
'''
s={'html','css','python','css','java','c++','js'}
#print(len(s))      #removes duplicates
c=0
for i in s:
    c+=1
print('length of set:',c)
'''
#5 union,intersection,difference
'''
s={11,13,17,19}
s1={2,4,6,8,10}
s2={1,3,5,7,9,10}
#s3=s1.union(s2)
s3=s1|s2
print('union:',s3)
#s4=s1.intersection(s2)
s4=s1&s2
print('intersection:',s4)
s5=s1.union(s2,s)  #s5=s1|s2|s
print(s5)
s6=s1.difference(s2)
print(s6)
s7=s1.symmetric_difference(s2) #s7=s1^s2
print(s7)
'''



'''

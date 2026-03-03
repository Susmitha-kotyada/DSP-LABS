import pandas as pd
'''s=pd.Series([10,20,30,40])
print(s)
print(s[0])
print(s[2])   #series behaves like an indexed array

#creating a series with custom index
a=pd.Series([89,95,85],index=['anu','arya','arha'])
print(a['arya'])

#creating a series from a dictionary
marks={'anu':89,'arya':90,'arha':85}
m=pd.Series(marks)
print(m)

#series attributes
s=pd.Series([10,20,30,40,50])
print(s.index)    #index values
print(s.values)   #data values
print(s.dtype)    #data type

#basic operations on series
s=pd.Series([10,20,30,40])
print(s+5)
print(s*2)
print(s)

#condition filtering
s=pd.Series([45,67,89,34,90])
print(s[s>50])

#checking for missing values
s=pd.Series([10,20,None,40])
print(s)
print(s.isnull())

#filling missing values
print(s.fillna(10))

#statistical functions
s=pd.Series([10,20,30,40,50])
print('sum=',s.sum())
print('mean=',s.mean())
print('max=',s.max())
print('min=',s.min())

#series vs list
s=pd.Series([1,2,3,4])
print(s>2)
print(s[s>2])   #using series
n=[1,2,3,4]
r=[]
for i in n:
    if i>2:
        r.append(i)
print(r)       #using lists'''

#DATA FRAMES
import pandas as pd
data={'Name':['anu','arya','arha'],
      'age':[25,28,26],
      'marks':[85,90,87]
      }
print(pd.DataFrame(data))
















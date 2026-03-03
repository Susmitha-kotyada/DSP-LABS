'''
file=open('Task1.py','r')
#file.write('hello world')
print(file.read())
'''
'''
with open('Task.txt','r+')as f:
    f.write('HI EVERYONE!\nI AM SUSMITHA KOTYADA')
    print(f.read())
'''
'''
with open('Task.txt','a+')as f:
    f.write('\nAN RGUKTN')
    print(f.read())
    '''
'''
f=open('Task.txt','w+')
#print(f.readline())
lines=['python\n','file operations\n']
f.writelines(lines)
print(f.readlines())
'''
'''
import os
print(os.getcwd())   #current working directory
#os.mkdir('myfolder')
print(os.listdir())
print(os.path.isfile('Task.txt'))
print(os.path.isdir('Task.txt'))
print(os.path.exists('Task.txt'))
os.rename('Task.txt','task.txt')
#os.rmdir('myfolder')     #returms error
for file in os.listdir():
    if file.endswith('.py'):
        print(file)
f=open('task.txt','r')
print(f.read(6))
f.seek(5)
print(f.tell())
'''

import re
text='python is an object 115oriented programming 23language'
m1=re.search('object',text)  #fnd first match anywhere
print(m1)
m2=re.match('object',text)   #matches only at the beginnning
print(m2)

result=re.findall('[labci]ng',text)
print(result)
rem=re.findall('\\d+',text)
print(rem)
mob='9865431240'
if re.fullmatch('[6-9]\\d{9}',mob):
    print('valid m_num')
else:
    print('invalid')

email='susmitha05@rguktn.ac'
if re.fullmatch(r'^\w+@[\w\.]+\.\w+$',email):
    print('valid')
else:
    print('invalid')

import numpy as np
print(np.array([11,23,22]))

#!/usr/bin/env python
# coding: utf-8

# In[3]:


n=int(input("enter lenght of fibbonaci series "))
a=0
b=1
print(a)
print(b)
for x in range(0,n):
    c=a+b
    print(c)
    a=b
    b=c


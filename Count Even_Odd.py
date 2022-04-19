#!/usr/bin/env python
# coding: utf-8

# In[1]:
#Method 1

series = [1,2,3,4,5,6,7,8,9]
oddno = 0
evenno = 0
for i in series:
        if (i % 2)==0:
            evenno+=1
        else:
            oddno+=1
print("Number of even numbers :",evenno)
print("Number of odd numbers :",oddno)


# In[ ]:

#Method2
series = int(input("Enter your number"))
oddno = 0
evenno = 0
for i in range(1,series+1): #It considers from 1 till user input
        if (i % 2)==0:
            evenno+=1
        else:
            oddno+=1
print("Number of even numbers :",evenno)
print("Number of odd numbers :",oddno)



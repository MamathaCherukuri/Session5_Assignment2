#!/usr/bin/env python
# coding: utf-8

# 1.Write a function to compute 5/0 and use try/except to catch the exceptions. 

# In[7]:


def div(a, b):
    try:
        a/b
    except ZeroDivisionError:
        print("Zero Division Error detected")
    else:
        print("No Zero Division Error")
    finally:
        print("Finally the division of %d/%d is done" % (a, b))


# In[8]:


div(1,1)


# In[9]:


div(1,0)


# 2.Implement a Python program to generate all sentences where subject is in ["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in ["Baseball","cricket"]. 
# Hint: Subject,Verb and Object should be declared in the program as shown below. 
# subjects=["Americans ","Indians"] verbs=["play","watch"] objects=["Baseball","Cricket"] 
# 

# In[10]:


subject=["Americans","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]

# Using nested looping to produce the expected result/output
for i in subject:
    for j in verbs:
        for k in objects:
            print(i+" "+j+" "+k+".")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[13]:


import math
import sys
import argparse


# In[20]:


def arrcheck(arr):
    c = 0
    for i in range(len(arr)):
        if not isinstance(arr[i], list):
            c = c + 1
    if c == len(arr):
        return 1
    else:
        return 0


# In[21]:


def flat(arr):
    i=0
    while i<30:
        i += 1
        M = []
        if isinstance(arr[i], list):
            le = len(arr[i])
            for j in range(le):
                M.append(arr[i][j])
            for s in range(le):
                arr.insert(i + s, M[s])
            del arr[i + s + 1]
            if i == len(arr)-1:
                i = 0
        if arrcheck(arr):
            break
    print("Your array = ", arr)


# In[101]:


def main():
    a=[1,2,[[[[[[[[2]]]]]]]]]
    print(a)
    flat(a)


# In[102]:


if __name__ == "__main__":
    main()


# In[18]:


parser = argparse.ArgumentParser(description='Great Description To Be Here')


# In[19]:


parser.add_argument('-l','--list', nargs='+', help='<Required> Set flag', required=True)


# In[27]:


obj = []
if len(sys.argv) > 1:
    obj =(sys.argv[1]) 


# In[93]:


d=input().split(' ')


# In[90]:


d


# In[60]:


def inp(arr):
    f=[]; i=0
    for i in len(arr):
        if arr[i]=='[':
            for j in range(50):
                if arr[i+j]==']':
                    break
                f.append(arr[i+j])
        else:
            f.append(arr[i])
    return f


# In[61]:


a=inp(d)


# In[96]:


f=[]
for i in range(len(d)):
    if not d[i].isdigit:
        for j in range(50):
            if not d[i+j+1].isdigit:
                break
            f.append(int(d[i+j]))
    else:
        f.append(d[i])
    print("f=", f)


# In[84]:


f


# In[94]:


d


# In[98]:


if not d[0].isdigit():
    print("a")


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# # Understand and explain how break will work in nested loop.

# * Nested Loop the break statement can be used to exit out of a loop at any level of nesting, and outer loops will be continue executed, if the break statement is executed inside an outer loop.

# In[56]:


for i in range(5):
    for j in range(5):
        if i == j:
            break
        print(i,j)

Output
1 0
2 0
2 1
3 0
3 1
3 2
4 0
4 1
4 2
4 3

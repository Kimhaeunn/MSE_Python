#!/usr/bin/env python
# coding: utf-8

# In[43]:


import numpy #소수점간격으로 출력하기 위해서는 numpy.arrange가 필요하다. 이를 위해서 import로 numpy함수를 열어준다.
for i in numpy.arange(0,5,0.1):#for문에 의해서 0부터 5가 되기 전까지 0.1 간격으로 i가 출력된다.
    print(i)   


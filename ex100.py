#!/usr/bin/env python
# coding: utf-8

# In[6]:


data=['09/05', '09/06', '09/07', '09/08', '09/09']
close_price=[10500,10300,10100,10800,11000]
close_table= dict(zip(data,close_price))#zip함수는 zip(a,b)에서 a,b리스트를 순차적으로 맞춤을 통해서 새로운 리스트를 만들어내고 이를 dict를 통해 딕셔너리로 생성한다.
print(close_table)


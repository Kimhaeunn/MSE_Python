#!/usr/bin/env python
# coding: utf-8

# In[46]:


class OMG:
    def print():
        print("Oh my god")
        
mystock=OMG
mystock.print() #print의 인자가 없으면 파이썬은 OMG.print(mystock)인식하게 되어 def print()로 정의되어야 하는데 def print()에는 객체인 mystock이 존재하지 않기 때문에 오류가 발생한다.


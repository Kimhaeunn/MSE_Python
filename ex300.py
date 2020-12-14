#!/usr/bin/env python
# coding: utf-8

# In[67]:


per = ["10.31", "", "8.00"]

for i in per: #리스트 per안의 원소들을 i에 하나씩 대입한다,
    try:# 실행코드
        print(float(i))
    except:#예외가 발생하였을 때 수행할 코드
        print(0)
    else:#예외가 발생하지 않았을 때 수행할 코드
        print("clean data")
    finally:#예외 발생 여부와 관계없이 항상 수령할 코드
        print("변환 완료")


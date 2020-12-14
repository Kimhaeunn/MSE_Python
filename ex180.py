#!/usr/bin/env python
# coding: utf-8

# In[10]:


low_prices=[100,200,400,800,1000]
high_prices=[150,300,430,880,1000]

volatility=[]#volatility라는 리스트에 저장하기 위해 작성
for i in range(len(low_prices)) :#range범위는 low_prices의 원소 수 만큼 
    volatility.append(high_prices[i]-low_prices[i])# 추가할 떄 사용하는 append함수를 이용하여 for문으로 들어오는 i로 구한 값을 volatility리스트에 추가해 하나씩 저장한다.
                                                   #high_prices[i] 리스트에서 i-1번째의 값을 도출해낸다. ex)high_prices[0]=150(파이썬은 0부터 카운트)
                                                   
print(volatility)                                       


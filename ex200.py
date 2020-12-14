#!/usr/bin/env python
# coding: utf-8

# In[20]:


ohlc=[["open","high","low","closed"],
     [100,110,70,100],
     [200,210,180,190],
     [300,310,300,310]]


for row in ohlc[1:]: #ohlc리스트에 원소로 존재하는 리스트들을 row에 하나씩 대입 한다.
                     #ohcl[1:]s는 ohcl의 원소인 첫번째 리스트부터 마지막 리스트까지를 뜻한다.
    profit+=(row[3]-row[0])#profit은 row의 세번째와 영번째, 즉 "closed"와 "open"의 차를 모두 더한 것이다.
                           #+=는 추가로 계속 더한다는 뜻이다.
print(profit)


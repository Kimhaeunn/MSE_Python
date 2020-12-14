#!/usr/bin/env python
# coding: utf-8

# In[15]:


apart=[[101,102],[201,202],[301,302]]

for row in apart:#apart리스트에 담긴 리스트들을 row에 하나씩 대입한다.
    for col in row:#apart리스트에 담긴 리스트들의 원소를 col에 대입한다.
        print(col,"호")#col과 "호"를 함께 출력한다.
print("-----")


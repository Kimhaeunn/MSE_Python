#!/usr/bin/env python
# coding: utf-8

# In[6]:


result = 1
for i in range(1,11): #range(1,11)은 1부터 10번까지의 숫자를 의미하므로 for문을 이용하여 1부터 10을 하나씩 i에 대입한다.
    result=result*i # i에 10까지의 숫자가 계속 대입되면서 1부터 10까지의 숫자가 모두 곱해진 결과가 나온다.
print(result)


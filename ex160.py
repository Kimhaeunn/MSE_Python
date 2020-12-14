#!/usr/bin/env python
# coding: utf-8

# In[5]:


리스트 = ['intra.h','intra.c', 'define.h', 'run.py']
for i in 리스트: #리스트에서 원소를 하나씩 뺴서 i에 대입한다.
    split= i.split(".")  #split는 split(a)일 때 a를 기준으로 원소들을 쪼갠다.
    if (split[1] == "h") or (split[1]=="c") : #split[1]: 쪼갠 뒤의 첫번째 문자
                                              #if 함수 내에서 주어진 조건, 즉 비교연산자 or을 통하여 주어진 두개의 확장자 중 하나라도 만족하면 출력한다.
        print(i)


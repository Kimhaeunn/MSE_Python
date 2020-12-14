#!/usr/bin/env python
# coding: utf-8

# In[39]:


def 함수0(num):
    return num*2

def 함수1(num):
    return 함수0(num+2)

def 함수2(num):
    num=num+10
    return 함수1(num)

#print(함수2(2))가 입력되었으므로 함수2(num)으로 정의된 과정을 통하여 num=2+10, 그리고 return함수에 의하여 함수1(num)으로 들아간다.
#함수1(num)으로 들아온 함수는 함수1(num)의 정의에 의해서 함수2(num)에서 계산을 통해 얻은 12을 num으로 하여 12+2=14를 얻게된다. 그리고 return함수에 의하여 함수0(num)으로 들어간다.
#함수0(num)으로 들어온 함수는 함수0(num)의 정의에 의해서 함수1(num)에서 계산을 통해 얻은 14를 num으로 하여 14*2=28을 얻게된다.

c=함수2(2)
print(c)


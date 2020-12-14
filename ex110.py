#!/usr/bin/env python
# coding: utf-8

# In[8]:


if True: #입력된 공백은 참임을 판별할 수 없음
    if False: #참임을 판별할 수 없어 처음 if True함수에 종속된 if False함수로 넘어왔지만 공백은 거짓임을 판별할 수 없다.
        print("1")
        print("2")
    else: #if False 함수에서 판별이 불가했기 때문에 else로 넘어와 else의 결과가 출력된다.
        print("3")
else:#처음 if True함수에 종속된 if False함수에서 결과가 나왔기 때문에 출력되지 않는다.
    print("4")
print("5")#위 함수들과 상관없이 독립적으러 "5"를 출력한다.


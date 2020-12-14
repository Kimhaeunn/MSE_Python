#!/usr/bin/env python
# coding: utf-8

# In[36]:


def print_max(a,b,c): #prin_max(a,b,c)가 입력되었을 때 다음과 같이 진행되도록 def를 통하여 정의한다.
    
    if a>b and a>c: #if함수를 통해 a가 b보다도 크고 c보다도 커 비교연산자 and의 조건이 만족되면 a를 출력한다. 
        print(a)
        
    elif b>c and b>a: #if함수에서 조건에 거짓되었 때 elif를 통하여 다를 조건에 한번 더 참거짓을 판별한다.
                      #b가 c와 a보다 크면 b를 출력한다
        print(b)
    else:
        print(c) #else에서는 if와 elif에서 모두 조건에 만족하지 못하였을 때 출력된다.
                 #a와 b가 가장 크다는 조건을 만족하지 못하였을 때는 자동적으로 c가 가장 큰 수이므로 c를 출력한다.


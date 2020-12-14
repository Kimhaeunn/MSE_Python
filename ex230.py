#!/usr/bin/env python
# coding: utf-8

# In[37]:


def my_print(a,b): #def함수를 통하여 my_print(a,b)가 입력되었을 때 다음과 같이 진행되도록 정의한다.
    print("왼쪽:",a)
    print("오른쪽:",b)
    
my_print(b=100,a=200) #주어진 a와b를 정의된 함수에 대입한다.
                      #a와 b를 명시적으로 표현해주었기 때문에 순서가 바뀌어도 상관없다.


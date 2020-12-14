#!/usr/bin/env python
# coding: utf-8

# In[66]:


class 부모:
  def __init__(self):#def와 생성자 init을 이용해서 생성자인수를 정의한다.
    print("부모생성")

class 자식(부모):
  def __init__(self): #def와 생정자 init을 이용해서 생성자인수를 정의한다
    print("자식생성")
    super().__init__()#super()를 통해 명시적으로 부모class를 호출한다.

나 = 자식()#자식class가 실행되므로 자식생성이 출력되고 그 후 super()에 의하여 부모class가 실행되므로 부모생성이 출력된다.


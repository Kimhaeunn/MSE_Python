#!/usr/bin/env python
# coding: utf-8

# In[54]:


class Stock:#객채 생성을 위하여 class생성
    def __init__(self,name,code, per,pbr,dividend): #생성자init을 통하여 생성자인수들을 정의한다.
        self.name=name#self는 만들어지는 객체를 의미한다.
        self.code=code
        self.per=per

종목=[]

삼성=Stock("삼성전자", "005930",15.79,1.33,2.83)
현대차=Stock("현대차", "005380",8.70,0.35,4.27)
LG전자=Stock("LG전자", "066570",317.34,0.69,1.37)

종목.append(삼성)#만들어둔 종목 리스트 안에 append함수를 이용하여 삼성을 추가한다.
종목.append(현대차)#만들어둔 종목 리스트 안에 append함수를 이용하여 현대차를 추가한다.
종목.append(LG전자)#만들어둔 종목 리스트 안에 append 함수를 이용하여 LG전자를 추가한다.

for i in 종목:# for문을 이용하요 종목리스트에 있는 원소들을 i에 하나씩 대입한다.
    print(i.code, i.per)


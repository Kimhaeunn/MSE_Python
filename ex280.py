#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[65]:


import random #import함수를 이용하여 random함수를 가져온다.


class Account:
    account_count = 0

    def __init__(self, name, balance): #생성자 init을 사용하여 생성자인수를 정의한다
        self.deposit_count = 0 #self는 만들어지는 객체를 의미한다.
        self.deposit_log = []
        self.withdraw_log = []

        self.name = name
        self.balance = balance
        self.bank = "SC은행"

        
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2) 
        num3 = str(num3).zfill(6) 
        self.account_number = num1 + '-' + num2 + '-' + num3
        Account.account_count += 1

    
    def get_account_num(cls):#get_account_num(cls)를 입력하면 아래와 같이 출력되도록 정의한다.
        print(cls.account_count)

    def deposit(self, amount):#deposit(self,amount)를 입력하면 아래와 같은 과정이 진행되도록 정의한다.
        if amount >= 1: #만약 amount의 크기가 1보다 크거나 같으면 아래와 같이 진행한다.
            self.deposit_log.append(amount)
            self.balance += amount

            self.deposit_count += 1 #selg deposit_count는 1만큼 계속 더한다.
            if self.deposit_count % 5 == 0: #나눗셈의 몫이 0인 경우  self balabce에 1.01을 곱한다. 
                self.balance = (self.balance * 1.01)


    def withdraw(self, amount):#withdraw(self,amount)가 입력되면 아래와 같이 출력되도록 정의한다.
        if self.balance > amount:
            self.withdraw_log.append(amount)
            self.balance -= amount

    def display_info(self): #display_info(self)가 입력되면 아래와 같이 출력되도록 정의한다.
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", self.balance)

    def withdraw_history(self): #wirhdraw_history(self)가 입력되면 아래와 같이 출력되도록 정의한다.
        for amount in self. withdraw_log:#selg.withdraq_log리스트의 원소들을 amount에 대입한다
            print(amount)

    def deposit_history(self):#deposit_history(self)가 입력되면 아래와 같이 출력되도록 정의한다.
        for amount in self.deposit_log:#self.deposit_log리스트의 원소들을 amount에 대입한다.
            print(amount)


k = Account("Kim", 1000)
k.deposit(100)
k.deposit(200)
k.deposit(300)
k.deposit_history()

k.withdraw(100)
k.withdraw(200)
k.withdraw_history()


# In[ ]:





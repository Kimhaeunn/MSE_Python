#!/usr/bin/env python
# coding: utf-8

# In[29]:


def message1(): #def를 통해서 message1()이 입력되면 A를 출력하도록 정의한다.
    print("A")

def message2(): #def를 통해서 message2()이 입력되면 B를 출력하도록 정의한다.
    print("B")

def message3(): #def 통해서 message3()이 입력되면 다음과 같이 출력한다.
    for i in range(3): #range(3)이므로 i= 0,1,2
        message2()
        print("c")
                  #i는 0일 때 message2()와 print("c")로 B,C 출력
                  #i는 1일 때 위와 같이 B,C 출력
                  #i는 2일 때 위와 같이 B,C 출력   
    message1()#처음 def에서 정의했으므로 "A"출력
    
    #한줄 씩 B,C,B,C,A가 출력됨
    
    
message3()


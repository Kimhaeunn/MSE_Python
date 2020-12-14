#!/usr/bin/env python
# coding: utf-8

# In[ ]:


fruit={"봄":"딸기","여름":"토마토","가을":"사과"}
user= input("좋아하는 과일은?")
if user in fruits.values(): #if 함수를 이용하여 만약 사용자가 입력한 값이 fruits.valuse, 즉 딕셔너리 fruit의 value값이라면 "정답입니다"를 출력한다.
    print("정답입니다")
else:
    print("오답입니다") #사용자가 입력한 값이 딕셔너리 fruit의 value값이 아니라면 "오답입니다"를 출력한다.


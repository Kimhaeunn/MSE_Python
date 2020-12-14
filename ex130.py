#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests #import함수를 사용하여 requests함수를 받아온다.
btc= requests.get("https://api.bithumb.com/public/ticker/").jason()['data']

변동폭= float(btc['max_price'])-float(btc['min_price']) #float 함수를 이용해 자료를 실수형으로 변환시킨다
시가=float(btc['opening_price'])
최고가=float(btc['max_price'])

if (시가+변동폭) > 최고가: #만약 위에서 얻은 시가와 변동폭의 합이 최고가보다 크다면 "상승장"을 출력한다.
    print("상승장")
else: #만약 위에서 얻은 시가와 변동폭의 합이 최고가보다 크지 않다면 "하락장"을 출력한다.
    print("하락장")


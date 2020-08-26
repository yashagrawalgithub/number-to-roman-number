#!/usr/bin/env python
# coding: utf-8

# In[50]:


d1={0:'',1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX'}
d2={0:'',1:'X',2:'XX',3:'XXX',4:'XL',5:'L',6:'LX',7:'LXX',8:'LXXX',9:'XC'}
d3={0:'',1:'C',2:'CC',3:'CCC',4:'CD',5:'D',6:'DC',7:'DCC',8:'DCCC',9:'CM'}
d4={0:'',1:'M'}
class taker:
    def __init__(self,value):
        self.value=value

class sender(taker):
    def __init__(self,value):
        self.value=value
        self.fourth(value)
    def fourth(self,value):
        a=(value//1000)
        print(d4[a],end='')
        self.third(value%1000)
    def third(self,value):
        a=(value//100)
        print(d3[a],end='')
        self.second(value%100)
    def second(self,value):
        a=(value//10)
        print(d2[a],end='')
        self.first(value%10)
    def first(self,value):
        print(d1[value],end='')
    
b=int(input())
m=sender(b)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[5]:


text=input("nhap vao 2 so nguyen")
s= text.split()
n1=int(s[0])
n2=int(s[1])
if n1<n2:
    
    for i in range(n1,n2+1):
        if i%3==0and i%5==0:
            print("FizzBuzz")
        elif i%3==0:
            print("Fizz")
        elif i%5==0:
            print("Buzz")
        else:
            print(i)
else:
    print("so dau tien phai nho hon so thu hai")
    


# In[ ]:





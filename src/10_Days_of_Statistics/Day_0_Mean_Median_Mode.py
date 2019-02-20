'''
Created on Feb 18, 2019

@author: Aasif Multani
'''
count=input()
a=input()
rate=[]
rate=a.split()
for x in range(len(rate)):
    rate[x]=int(rate[x])

b=input()
amount=[]
amount=b.split()
for x in range(len(amount)):
    amount[x]=int(amount[x])

try:
    print(float(sum(rate[g] * amount[g] / sum(amount) for g in range(len(rate)))))
except:
    print(rate)
    print(amount)

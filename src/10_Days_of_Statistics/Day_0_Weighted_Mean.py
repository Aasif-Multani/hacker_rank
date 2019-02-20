'''
Created on Feb 19, 2019

@author: Aasif Multani
'''

from statistics import mean, median, mode

count=input()
a=input()
my_list=[]
my_list=a.split()
for x in range(len(my_list)):
    my_list[x]=int(my_list[x])
            
print(float(mean(my_list)))
print(float(median(my_list)))
flag =0
try:
    print(float(mode(my_list)))
except:
    print(sorted(my_list)[0])
    flag =1

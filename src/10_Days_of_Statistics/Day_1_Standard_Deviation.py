'''
Created on Feb 20, 2019

@author: Aasif Multani
'''

from statistics import stdev

count=input()
numbers=input()
my_list=[]
my_list=numbers.split()
for x in range(len(my_list)):
    my_list[x]=int(my_list[x])

print(stdev(my_list))

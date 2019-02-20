'''
Created on Feb 20, 2019

@author: Aasif Multani
'''

import pandas as pd
import numpy as np

count=input()
numbers=input()
my_list=[]
my_list=numbers.split()
for x in range(len(my_list)):
    my_list[x]=int(my_list[x])

print(np.percentile(my_list, 25))
print(np.percentile(my_list, 50))
print(np.percentile(my_list, 75))

df = pd.DataFrame(my_list, columns=['my_list'])
print(df.my_list.quantile([0.25,0.5,0.75]))
print(df.describe())

print((np.percentile(my_list, 75))-(np.percentile(my_list, 25)))

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

in_file = open ("rosalind_hamm.txt","r")


num = 0

result = [line.split() for line in in_file.readlines()]

l1 = str(result[0])
l2 = str(result[1])

list1 = l1[2:-2]
list2 = l2[2:-2]

for i in range(len(list1)):
    if list1[i] != list2[i]:
        num = num+1

print(num)

#for line in in_file:
    
    
    
    
    
        

    
    
    






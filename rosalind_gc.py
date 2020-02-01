# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

in_file = open ("rosalind_gc.txt","r")


tot = 0
CG = 0
AT = 0

sol = {}


for line in in_file:
    if line[0]==">":
        ros = (line[1:-1])
        
        tot = 0
        CG = 0 
        AT = 0
        
    else:
        for i in line:
            if i == "C" or i == "G":
            
                CG = CG + 1
                tot = tot + 1
            elif i == "T" or i =="A":
                tot = tot + 1
                AT = AT + 1
            ratio = (CG/tot)*100
            
    
        sol[ros]=ratio
        
        
    
k = ""
v = 0
             
for key, value in sol.items():
    
    if value > v:
        v = value
        k = key
        
print (k +"\n" + str(v))
        

    
    
    






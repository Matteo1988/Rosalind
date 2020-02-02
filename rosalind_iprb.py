# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

k = 24
m = 21
n = 19

d = float(m+n+k)

#calculate the probability of getting a recessive trait

first = (m/(2*d)) * ((m-1)/(2*(d-1)) + (n/(d-1)))

second = (n/d) * (m/(2*(d-1))+((n-1)/(d-1)))


# the solution is 1 - the probability of getting a recessive trait

p = 1 - (first+second)

print(p)



    
    
    
    
    
        

    
    
    






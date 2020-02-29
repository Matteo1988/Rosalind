#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 09:46:27 2020

@author: matteobellini
"""


from Bio import SeqIO


import numpy as np

m = []
for sequence in SeqIO.parse("rosalind_cons.txt", "fasta"):
    
    dna_list = sequence.seq

    l = []
    for i in dna_list:
        
        l.append(i)
        
    m.append(l)
    


    #convert a matrix into a numpy matrix


M = np.array(m).reshape(len(m),len(m[0])) # if i use M = nm.matrix(m) len(M[0]) = 1


A = []
C = []
G = []
T = []

for i in range(len(M[0])):
    
    a = 0
    c = 0
    g = 0
    t = 0
    
    for j in M[:,i]:
        
        if j == "A":
            
            a = a+1
        
        elif j == "C":
            
            c = c+1
        
        elif j == "G":
            
            g = g+1
            
        elif j == "T":
            
            t = t+1
            
    A.append(a)
    C.append(c)
    G.append(g)
    T.append(t)


b = []

b.append(A)
b.append(C)
b.append(G)
b.append(T)    

sol = ""

# devo fare così, se faccio come psopra non va

B = np.array(b).reshape(4, len(A))
solution = ""
for i in range(len(A)):
    if max(B[:,i]) == B[0,i]:
        solution=solution+"A"
    elif max(B[:,i]) == B[1,i]:
        solution=solution+"C"
    elif max(B[:,i]) == B[2,i]:
        solution=solution+"G"
    elif max(B[:,i]) == B[3,i]:
        solution=solution+"T"


print(solution)

"""""

B = np.array(b).reshape(len(b),len(b[0]))

for k in range(len(B[0])):
    
    for l in B[:,k]:
        
        print(l)
    
 
    
    if max(B[:,k]) == [0,k]:
        
        sol = sol+" "+"A"
     
    if max(B[:,k]) == [1,k]:
        
        sol = sol+" "+"C"
    
        
    if max(B[:,k]) == [2,k]:
        
        sol = sol+" "+"G"
        
    if max(B[:,k]) == [3,k]:
        
        sol = sol+" "+"T"
        
print(sol)
    
    
    """
    
    

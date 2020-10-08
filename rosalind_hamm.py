with open("rosalind_hamm.txt","r") as f:
    seq = f.read()
    
print(seq)
l = list(seq.split("\n"))
print(l)
s1 = l[0]
s2 = l[1]

print(s1)
print(s2)

dist = 0

for i in range(len(s1)):
    if s1[i] != s2[i]:
        dist = dist+1
        
print(dist)

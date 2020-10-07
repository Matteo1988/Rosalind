with open("prova.txt","r") as f:
    s = f.read()
print(s)

l = []
for i in range(len(s)):
    if s[i]=='A':
        l.append('T')
    if s[i]=='C':
        l.append('G')
    if s[i]=='G':
        l.append('C')
    if s[i]=='T':
        l.append('A')

comp = ""

for ele in l:
    comp = comp+ele



rev = comp[::-1]

print(rev)

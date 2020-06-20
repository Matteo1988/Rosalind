#two offspring I have to *2
P1 = 1*2 #always dominant (AA)
P2 = 1*2 #always dominant (AA or Aa)
P3 = 1*2 #always domninant (Aa)
P4 = 0.75*2 # 25% -> AA 50% -> Aa 25% -> aa
P5 = 0.5*2 # 50% Aa and 50% aa
P6 = 0*2 #always recessive (aa)

rosalind = open ("rosalind_iev.txt","r")

for line in rosalind:
    line = line.strip()
    population =list(line.split(" "))

    print(population)

sol = P1*(int(population[0]))+P2*(int(population[1]))+P3*(int(population[2]))+P4*(int(population[3]))+ P5 * (int(population[4]))

print(sol)

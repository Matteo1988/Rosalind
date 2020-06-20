

import math

def indipendent_alleles(k, N):

    P = 2**k

    probability = 0

    for i in range (N, P+1):

        prob = (math.factorial(P))/(math.factorial(i)*math.factorial(P -i))*0.25**i * (0.75**(P-i))

        probability = probability + prob

    return(probability)


if __name__ == "__main__":

    print(indipendent_alleles(7,31))

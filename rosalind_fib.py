with open("rosalind_fib.txt","r") as f: #import file from rosalind
    s = f.read()

l = list(s.split(" ")) #convert string to a list

l[-1] = l[-1].strip() # remove the final \n

n_months=int(l[0])
k_el=int(l[1])


def fibonacci(n,k):
    if n == 1 or n == 0:
        return n
    else:
        return fibonacci(n-1,k)+fibonacci(n-2,k)*k
    
fibonacci(n_months, k_e

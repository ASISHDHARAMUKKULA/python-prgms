def factors(n):
    factorslist=[]
    for i in range(1,n+1):
        if n%i==0:
            factorslist=factorslist+[i]
    return factorslist
def prime(n):
   return factors(n) == [1, n]
def primelist(n):
    primelist=[]
    for i in range(1,n+1):
        if(prime(i)):
            primelist=primelist+[i]
    return primelist
r=factors(10)
print(r)
y=prime(25)
print(y)
z=primelist(25)
print(z)

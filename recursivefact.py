def fact(n):
    if(n==0):
         result=1
    else:
         result=n*fact(n-1)
    return result
print(fact(2))
print(fact(0))
print(fact(4))

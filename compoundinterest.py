import math
def compoundinterest(p,r,t):
    amount=p*(math.pow((1+(r/100)),t))
    print("compound amount:",amount)
    ci=amount-p
    return ci
p=float(input("enter principal amount"))
r=float(input("enter the rate of interest"))
t=float(input("enter time period"))

print("compound interest is",compoundinterest(p,r,t))

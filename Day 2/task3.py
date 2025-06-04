# waf to find the factorial of n,(n is a parametr)
def fact(num):
    fac=1
    for i in range(1,num+1):
        fac *=i
        i+=1
    print(fac)
        
fact(3)
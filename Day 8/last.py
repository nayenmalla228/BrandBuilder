# you can catch multiple errors

try:
    
    b=int(input("enter b:"))
    num=10/b

except(ZeroDivisionError,ValueError,TypeError) as e:
    print("Error",e)
#using else and finally

try:
    num=int(input("enter a number:"))
    result=10/num
except ZeroDivisionError:
    print("you cant divide a number by zero")
except ValueError:
    print("you entered wrong value")
else:
    print("result is",result)
finally:
    print("check the error")  #this finally part always run
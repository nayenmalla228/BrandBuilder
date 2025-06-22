#handling specific error

try:
    a=int(input("enter a number:"))
except ValueError:
    print("you entered the wrong value")
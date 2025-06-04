#working on function
# There are 3 types of functions
#1 built-in functions
#2 user defined functions

def add(a,b):
    """ this function add two number"""
    return a+b

print (add(4,5))

c=int(input("enter first no:"))
d=int(input("enter second no:"))
m=add(c,d)
print(m)

def sub(a,b):
    # """ subtract two numbers"""
    return a-b

print(sub(6,2))

def hello(): # print hello world by calling hello()
    print("hello world")

hello() #calling function

def add(a,b):
    print(a+b)
    
add(4,2)    

def sub(a,b):
    print(a-b)
    
sub(4,5)    

def mul(a,b):
    return a*b
print(mul(3,3))



    
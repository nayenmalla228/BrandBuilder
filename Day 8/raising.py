# we can raise our own exception.

age=int(input("Enter the age:"))
if(age<18):
    raise ValueError("you must be older than 18")
else:
    print("you are eligible to vote")
    
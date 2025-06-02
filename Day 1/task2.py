#wap to enter age if less then 18,kid,18< young ,more then 70 then old
age=int(input("enter the age"))
if(age<18):
    print("you are kid")
elif(age>18 and age<70):
    print("you are young")
else:
    print("you are old")
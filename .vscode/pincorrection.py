pin=6381
chances=1
print("you have three chances to enter the correct pin")
while chances<=3:
    pin=int(input("enter your 4 digit pin:-"))
    if(pin==6381):
        print("correct")
        break
    else:
        print("incorrect")
        chances+=1
else:
    print("your account is blocked")
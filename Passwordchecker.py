OG_password="admin@123"
password=input("Enter Your Password: ")
No_of_Attempts=3
if(OG_password ==password):
    print("Access Granted !")
else:
    No_of_Attempts-=1
    print("Access Denied ! You have only",No_of_Attempts,"more attempts left.")

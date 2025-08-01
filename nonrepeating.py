name=input("Enter any Name:- ")
for char in name:
    if name.count(char) == 1:
        print("First non-repeating character:", char)
        break
    else:
         print("No non-repeating character found.")

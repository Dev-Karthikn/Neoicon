names = []

while len(names) < 5:
    name = input("Enter a name: ")
    if name in names:
        print("Name already entered. Try a different one.")
    else:
        names.append(name)

print("\nUnique names entered:")
for i in range(5):
    print(names[i])

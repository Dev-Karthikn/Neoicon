# from collections import Counter
# password=input("Enter your Password:- ").lower()
# frq=Counter(password)
# pass_word={}
# for i in frq.items():
#    pass_word.append(i)
# print(pass_word)
  




from collections import Counter

password = input("Enter your password: ")
freq = Counter(password)
print("\nPassword accepted!")
print("\nCharacter frequencies:")
for k, v in freq.items():
    print(f"'{k}': {v}")

weak = False
for count in freq.values():
    if count >= 3:
        weak = True
        break
max_count = max(freq.values())
if weak:
    print(f"\nWeak password detected!,a Character repeated {max_count} times,Please choose a different one.")
else:
    print("\nPassword is strong enough.")

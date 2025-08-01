# Voting_age= input("Enter Your age :- ")
# a=int(Voting_age)
# voters=list([])
# for i in a:
#     if(i>18):
#         voters.append(i)
#         print("Eligible Voters are:",voters)
#     else:
#         print("You are not eligible to vote")



ages = list(map(int, input("Enter all ages (separated by spaces): ").split()))


results = []
eligible_count = 0

for age in ages:
    if age > 18:
        results.append("Eligible")
        eligible_count += 1
    else:
        results.append("Not Eligible")

# Output
print("\nEligibility Results:", results)
print("Total number of eligible voters:", eligible_count)


# def max_args(*args):
#     sum=0
#     for i in args:
#         sum+=i
#     print("sum is",sum)
# max_args(34,34)
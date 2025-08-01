# from collections import Counter
# name=['red','blue','green','red','yellow','black','white','red','pink','orange','purple']
# freq=Counter(name)
# for k,v in freq.items():
# 	print(k,'=',v)
# print(freq)


#each character frequency of string
from collections import Counter
name="pseudopodia"
frq=Counter(name)
print(frq)
for i,j in frq.items():
      print(f"{i} is repeated {j} times")
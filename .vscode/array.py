# # # from array import *
# # # arr=array('i',[1,2,3,4,4,5,])
# # # print(arr.buffer_info())
# # # print(arr.__getstate__())

# # # for j in range(0,len(arr)):
# # #     print(j,end=" ")


# # import numpy as np
# # arr=np.array([1,2,3,4])
# # print(arr*3)



# word="mississippi"
# for i in set(word):
#     print(i.upper(),"repeated:- ",word.count(i),"times")


def palindrome(s):
    if s==s[::-1]:
        return(s.capitalize(),"It is Palindrome")
    else:
        return(s.upper(),"Not a Palindrome")
print(palindrome("maiam"))
# sm = lambda x : x + 15
# print(sm(1))
#
# mul = lambda x,y:x*y
# print(mul(2,3))
#
# db = lambda x:x*2
# print(db(5))
#
# lst = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# sorted(lst,key=lambda x:x[0])
# print(lst)



# tup =(1,2,3,4,6)
# for index,value in enumerate(tup,start=1):
#     print(value,index)
#
# l1 = ["eat", "sleep", "repeat"]
#
# # printing the tuples in object directly
# for ele in enumerate(l1):
#     print(list(ele))

# def newmethod():
#     print("i love you")
# # newmethod()
# if __name__ == '__main__':
#     newmethod()
#
# x,k=map(int,input().split(" "))
# print(x,k)
# n = int(input())
# lst=[]
# for i in range(0,n):
#     item=int(input())
#     lst.append(item)
# print(lst)
# if (all(lst)>0):
#     print(True)

# CODING/DECODING
#\\\\if the word contains atleast 3 characters,
# remove the first letter and append it at the
# end now append three random characters at the starting and the end
# else: simply reverse the string\\\\\\\\\

# if the word contains less than 3 characters, reverse it
# else: remove 3 random characters from start and end.
# Now remove the last letter and append it to the beginning
import random
import string
str = input()
lst=str.split(" ")
new = []
decode = input("Enter 1 for coding and 0 for decoding:")
True if decode == 0 else False
if decode ==True:
    for ele in lst:
        if len(ele)>=3:
            ele=ele[1:]+ele[0]
            res = ''.join(random.choices(string.ascii_letters, k=3))
            ele=res+ele+res
            new.append(ele)
        else:
            ele = ele[::-1]
            new.append(ele)
    print(" ".join(new))
else:
    for ele in lst:
        if len(ele)>=3:
            ele=ele[3:-3]
            ele=ele[-1]+ele[0:-1]
            new.append(ele)
        else:
            new.append(ele[::-1])
    print(" ".join(new))



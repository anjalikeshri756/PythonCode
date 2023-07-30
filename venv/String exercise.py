#Write a Python program to count the number of characters (character frequency) in a string.
str = "google.com"
dic={}
for i in range(0,len(str)):
    cnt=str.count(str[i])
    dic.update({str[i]:cnt})
print(dic)

#3. Write a Python program to get a string made of the first 2 and last 2 characters of a given string.
# If the string length is less than 2, return the empty string instead
# str=input()
# if len(str)>1:
#     first= len(str)-2
#     last = len(str)
#     new=str[0:2]+str[first:last]
#     print(new)
# else:
#     print("")
#
#Write a Python program to get a string from a given string where all occurrences
# of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'


def change_char(str1):
  char = str1[0]
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:]

  return str1

print(change_char('restart'))

#5. Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

def char_mix(a,b):
    new_a=b[:2]+a[2:]
    new_b=a[:2]+b[2:]
    return new_a+ " "+new_b

new = char_mix('abc','xyz')
print(new)

#Write a Python program to add 'ing' at the end of a given string
# (length should be at least 3). If the given string already ends
# with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

def str_ing_ly(a):
    if a.endswith('ing') :
        lst=a.split()
        lst.append('ly')
        a="".join(lst)
        return a
    if a.endswith('ing') !=True and len(a)>=3:
        a=a+'ing'
        return a
str = str_ing_ly('abc')
print(str)

#7. Write a Python program to find the first appearance of the substrings
# 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the
# whole 'not'...'poor' substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'
def appearance(str):
    not_indx=str.find('not')
    poor_indx=str.find('poor')

    if not_indx<poor_indx and not_indx!=0 and poor_indx!=0:
        str=str.replace(str[not_indx:(poor_indx+4)],'good')
        return str
    else:
        return str

ss=appearance('The lyrics is not that poor!')
print(ss)

# Write a Python function that takes a list of words and return the longest word and the length of the longest one.
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9

def longest_word(str):
    lst = str.split()
    dic={}
    for index,value in enumerate(lst):
        dic.update({len(value):value})
        # print(dic)
    max_key = max(dic,key=lambda x:dic[x])
    return(max_key,dic[max_key])


long,value=longest_word("The lyrics is good!")
print(long,value)

#9. Write a Python program to remove the nth index character from a nonempty string.
# def n_char_removal(str,n):
#     fs=str[:n]
#     ss=str[n+1:]
#     return fs+ss
# new = n_char_removal("ABCDEFGHIJK",5)
# print(new)

#Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.
# def char_exchange(str):
#     new=str[-1]+str[1:-1]+str[0]
#     return new
# new = char_exchange("ABCDEF")
# print(new)

#Write a Python program to remove characters that have odd index values in a given string.
# def remove_odd_index(str):
#     new=""
#     for i in range(len(str)):
#         if i%2==0:
#             new = new+str[i]
#     return new
# new = remove_odd_index("abcdef")
# print(new)

# x,y=map(int,input().split())
# if (x+y)<=6:
#     print("No")
# else:
#     print("Yes")
#
# T = int(input())
# for tc in range(T):
# # Read integers a and b.
#     (a, b) = map(int, input().split(' '))
#
# ans = a + b
# print(ans)

# t=int(input())
# for i in range(t):
#     x=int(input())
#     if (x<67 and x>45000):
#         print("No")
#     else:
#         print("Yes")

t=int(input())
lst=[]
for i in range(t):
    ele=list(map(int,input().split()))
    print(ele)
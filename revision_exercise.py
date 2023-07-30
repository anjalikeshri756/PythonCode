# str= "###hello World!!@!!"
# new="hello"
# # new = str.upper()
# # print(str.title())
# # print(str.capitalize())
# # print(str.lower())
# # print(str.casefold())
# # print(str.strip())
# # print(str.rstrip("!"))
# print(str.lstrip("#"))
# print(new)
# str1 = "hello"
# capStr1 = str1.capitalize()
# print(capStr1)
# str2 = "hello WorlD"
# capStr2 = str2.capitalize()
# print(capStr2)
#
# import datetime as dt
# now = dt.datetime.now()
# print ("Current date and time : ")
# print (now.strftime("%Y-%m-%d %H:%M:%S"))
# import math
# r=1.1
# p = math.pi
# area=p*r**2
# print(area)

# f=list(input().split(','))
# s=tuple(input().split(','))
# print(f)
# print(s)
# color_list = ["Red","Green","White" ,"Black"]
# for index,value in enumerate(color_list):
#     if index==0 or index==(len(color_list)-1):
#         print(value)
# exam_st_date = (11, 12, 2014)
# print(f"The examination will start from : {exam_st_date[0]}/{exam_st_date[1]}/{exam_st_date[2]}")
# n = int(input())
#
# print(eval(f"{n}+{n}{n}+{n}{n}{n}"))
num= lambda x:bool(x%3)
print(num(23),num(21))
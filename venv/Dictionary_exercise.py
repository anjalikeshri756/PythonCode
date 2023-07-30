# dic={1:121,2:212,3:313}
# print(dic[1])
# print(dic.get(1))
# for i in dic.keys():
#     print(i)
# for i in dic.values():
#     print(i)
# for key, value in dic.items():
#     print(f"key is {key} and value for that is {value}")
#
# dic1={11:111,22:222}
# dic.update(dic1)
# print(dic)
#
# dic.pop(11)
# print(dic)
#
# dic.popitem()
# print(dic)
#
# dic3 = dic.copy()
# print(dic3)
#
# # del(dic3)
# # print(dic3)
#
# x=(1,2,3,4,5)
# y=None
# new=dict.fromkeys(x,y)
# print(new)
#
# def sort_dict_by_keys(**num):
#     lst = list(num.keys())
#     lst.sort()
#     dic_final={}
#     for key in lst:
#         dic = {}
#         # print(f"sorted dictionary:{key}:{num['key']}")
#         dic={key:num[key]}
#         dic_final.update(dic)
#     return dic_final
#
# result = sort_dict_by_keys(mname="Buchanan", lname="Arnes", fname="James")
# print(result)
#
#
# sort
# dic = {1:22,21:23,2:34}
# lst = list(dic.keys())
# print(lst)
# lst.sort(reverse=False)
# print(lst)
# new = {i:dic[i] for i in lst}
# print(new)

# dictionary containing longitude and latitude of places
# places = {("19.07'53.2", "72.54'51.0"):"Mumbai", \
# 		("28.33'34.1", "77.06'16.6"):"Delhi"}
#
# # Traversing dictionary with multi-keys and creating
# # different lists from it
# lat = []
# long = []
# plc = []
# for i in places:
# 	lat.append(i[0])
# 	long.append(i[1])
# 	plc.append(places[i[0],i[1]])
#
# print(lat)
# print(long)
# print(plc)
# from operator import itemgetter
# dic =  [{"name": "Nandini", "age": 20},
#        {"name": "Manjeet", "age": 22},
#        {"name": "Nikhil", "age": 20}]
# print(sorted(dic,key=itemgetter('age')))
# # list = list(dic.values())
# # list.sort(reverse=False)

#merge 2 dictionary
# dic1={"name": "Nandini", "age": 20}
# dic2={"address": "Delhi"}
# dic1.update(dic2)
# print(dic1)

#max unique value for a key
# test_dict = {"Gfg": [5, 7, 5, 4, 5],
#              "is": [6, 7, 4, 3, 3],
#              "Best": [9, 9, 6, 5, 5]}
# for i in test_dict.values():
#     print(f"actual length of values:{len(i)}")
#     print(f"length of unique elements in values list {len(set(i))}")


# if __name__ == '__main__':
#
#     # final_list=[]
#     # for _ in range(int(input())):
#     #     python_students = []
#     #     name = input()
#     #     score = float(input())
#     #     python_students.append([name,score])
#     #     final_list.append(python_students)
#     final_list = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
#     # print(final_list)
#     new =[]
#     new = sorted(final_list, key=lambda x: x[1])
#     # print(new)
#     # print(final_list)
#     if new[2][1]==new[1][1]:
#         new.sort(reverse=False)
#         # print(new)
#     print(new[1][0])
#     print(new[2][0])

# if __name__ == '__main__':
#     # num_of_ele=int(input())
#     # lst = []
#     # for i in range(num_of_ele):
#     #     ele=int(input())
#     #     lst.append(ele)
#     # tup = tuple(lst)
#     # print(tup)
#     # print(hash(tup))
#     n = int(input())
#     t = tuple(map(int, input().split()))
#     print(hash(t))

# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#     for key,values in student_marks.items():
#         if key == query_name:
#             avg=sum(values)/3
#             # print('%.2f' % avg)
#             print(f"{avg},.2f")
#
# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
#     lst =[]
#     for i in range(0,x+1):
#         for j in range(0,y+1):
#             for k in range(0,z+1):
#                 lst.append([i,j,k])
#     print(lst)
#     new=[]
#     for value in lst:
#         if sum(value) == 2:
#             continue
#         else:
#             new.append(value)
#     print(new)

# def mutate_string(string, position, character):
#     new = list(string)
#     new.insert(position,character)
#     new.pop(position+1)
#     s_new = "".join(new)
#     return s_new
#
#
# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)

# def count_substring(string, sub_string):
#     for i in range(0, len(string)):
#         print(string[i])
#
#
# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
#
#     count = count_substring(string, sub_string)
#     print(count)

# if __name__ == '__main__':
#     s = input()
#     print(True if s.isalnum() else False)

# import textwrap
#
#
# def wrap(string, max_width):
#     return textwrap.fill(string, max_width)
#
#
# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)
#
# num=10
# num.format()
#
# def solve(s):
#     lst = s.split()
#     new = []
#     for i in range(0, len(lst)):
#         if lst[i][0].isdigit():
#             new.append(lst[i])
#         else:
#             new.append(lst[i].title())
#     print(" ".join(new))
#
# if __name__ == '__main__':
#     # fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     s = input()
#
#     result = solve(s)


# try:
#     a = int(input)
# except ValueError as e:
#     raise(f"ValueError: invalid literal for int() with base 10: {a}")
# try:
#     b = int(input)
# except ValueError as e:
#     raise(f"ValueError: invalid literal for int() with base 10: {b}")
#     # fptr.write(result + '\n')
#
#     # fptr.close()
#
# sum = lambda x,y:x+y
# print(sum(2,3))

# import math
# ip=input()
# lst=ip.split("+")
# x=lst[0]
# y=lst[1][:-1]
# xs=int(x)**2
# ys= int(y)**2
# print(type(xs),type(ys))
# sm = xs+ys
# z=math.sqrt(sm)


# import calendar
# print(calendar.TextCalendar(firstweekday=6).formatyear(2015))
#
# import calendar
# y = int(input("Input the year : "))
# m = int(input("Input the month : "))
# print(calendar.month(y, m))

# from datetime import date
# f_date = date(2014, 7, 2)
# l_date = date(2015, 7, 11)
# delta = l_date - f_date
# print(delta.days)
# num = int(input())
# st = input().split()
# print(type(st))


# String compression
# st=input("enter a string:")
# count = 1
# compressed=[]
# for i in range(1,len(st)):
#     if st[i]==st[i-1]:
#         count=count+1
#     else:
#         compressed.append(st[i-1]+str(count))
#         count=1
# compressed.append(st[-1]+str(count))
# print("".join(compressed))

# vowel count
# vw=['a','e','i','o','u']
# num= int(input())
# string = input().split()
#
# lst=[]
# for i in string:
#     vcount = 0
#     for j in range(0,len(i)):
#         if i[j] in vw:
#             vcount+=1
#     lst.append(vcount)
# print(lst)
#
# new = [2 if x%2==0 else 1 for x in lst]
# sum=0
# for i in new:
#     sum=sum+i
# print(sum)










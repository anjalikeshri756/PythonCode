import os
# # os.mkdir("folder/data")
# f=open("folder/data/abc.txt",'w')
# str="Hello my name is Anjali /n"
# f.write(str)
# f=open("folder/data/abc.txt",'r')
# txt=f.read()
# print(txt)
# f.close()
#
# f=open("folder/data/abc.txt",'a')
# f.writelines("Hello baby")
# f.flush()

with open('sample.txt','w') as f:
    f.write("hello world")
    # f.truncate(5)

with open('sample.txt', 'r')as f:
    f.seek(6)
    cp=f.tell()
    print(cp)
    print(f.read())
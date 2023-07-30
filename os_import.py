import os
print(os.getcwd())
if not os.path.exists("folders"):
    os.mkdir("folders")
else:
    print("already exist")
dir = "folders"
for folder in os.listdir(dir):
    # os.mkdir(f"folders/folder {folder}")
    # os.rename(f"folders/folder {folder}",f"folders/folder {folder+1}")
    # os.remove("folder/new.md")
    file = f'file {folder}.txt'
    # with open(os.path.join(f"folders/{folder}", file), 'w') as fp:
    #     pass
    file1 = open(f'folders/{folder}/file {folder}.csv', 'w')
    L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
    s = "Hello\nI love You\n"

    file1.write(s)

    file1.writelines(L)

    file1.close()

    file1 = open(f'folders/{folder}/file {folder}.txt', 'r')
    print(file1.read())
    file1.close()
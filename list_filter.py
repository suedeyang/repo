fp=open("db.txt",'r')
stu_list=fp.readlines()
stu_list
print(stu_list)
if "10101\n" in stu_list:
    print("YES")
else:
    print("NO")
fp.close()
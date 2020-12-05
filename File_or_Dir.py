import os
allfiles = os.listdir('C:/')
print (allfiles)
list1=[]
list2=[]
for i in range(0,len(allfiles)):
    if os.path.isfile(allfiles[i]) == True:
        list1.append(allfiles[i])
    else:
        list2.append(allfiles[i])
print("Các file là:",list1, "Các thư mục là:", list2)
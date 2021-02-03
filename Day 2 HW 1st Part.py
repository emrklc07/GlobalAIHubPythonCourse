mylist = [1,2,3,4]
mylist[2], mylist[3] = mylist[0], mylist[1]

mylist1 = [1,2,3,4]
mylist1[0], mylist1[1] = mylist1[2], mylist1[3]

mylist2 = [mylist1[2],mylist1[3],mylist[0],mylist[1]]

print(mylist2)



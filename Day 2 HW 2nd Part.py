n = int(input("Enter a single digit integer: "))

n_string = str(n)

if type(n) != int or len(n_string) > 1:
    print("Invalid value!!")
else:
    mylist = list(range(0,n+1,2))
    print(mylist)





correct_info = {"username": "python", "password": "abcd123"}
info = {}

info["username"] = (input("Enter your username: "))

info["password"] = (input("Enter your password: "))


mylist = list(correct_info.values()) + list(info.values())

#index 0 is the correct username
#index 1 is the correct password
#index 2 is the entered username
#index 3 is the entered password

if mylist[0] == mylist[2] and mylist[1] != mylist[3]:
    print("The username is correct but the password is incorrect!")
elif mylist[0] != mylist[2] and mylist[1] == mylist[3]:
    print("The password is correct but the username is incorrect!")
elif mylist[0] != mylist[2] and mylist[1] != mylist[3]:
    print("Both username and password are incorrect!")
else:
    print("Logged in successfuly!")

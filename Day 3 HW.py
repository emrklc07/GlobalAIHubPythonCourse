username = "python"

password = "abcd123"

usrname = input("Enter your username: ")

pswrd = input("Enter your password: ")

if usrname != username and pswrd != password:
    print("Both username and password are incorrect!")
elif usrname == username and pswrd != password:
    print("The username is correct but the password is incorrect!")
elif usrname != username and pswrd == password:
    print("The password is correct but the username is incorrect!")
else:
    print("Logged in successfuly!")


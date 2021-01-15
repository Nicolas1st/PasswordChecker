from sys import argv


if len(argv) > 1:
    with open("password.txt", "r") as f:
        if f.read().strip() == argv[1].strip():
            print("The password is correct")
        else:
            print("The password is invalid")
else:
    print("You need to specify the password after the name of the program you are running")


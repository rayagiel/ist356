# the sentinel is the word "secret"

password = "secret"


for attempt in range(5):
    entered_password = input("Enter the password: ")
    if entered_password == password:
        print("Access granted!")
        break
    # exit(0) is success exit(1) is failure
    else:
        print("You are denied!")

    print(f"Attempt {attempt+1} of 5")
else:
    print("You are locked out!")


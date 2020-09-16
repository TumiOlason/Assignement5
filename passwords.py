
password = input("Enter a new password: ")
incorrect = 0
valid = 0
max_length = 20
min_length = 6
while password != "q":
    upper = False
    lower = False
    digit = False

    if len(password) >= min_length and len(password) <= max_length:
        for c in password:
            if c.isupper():
                upper = True
            elif c.islower():
                lower = True
            elif c.isdigit():
                digit = True

        if not lower:
            print("At least one lower case letter needed")
        if not upper:
            print("At least one upper case letter needed")
        if not digit:
            print("At least one number needed")
        if digit and lower and upper:
            valid += 1
            print("Valid password of length", len(password))
        else:
            incorrect += 1

    else:
        incorrect += 1
        print("Invalid length")

    password = input("Enter a new password: ")

print("You tried {} passwords, {} valid, {} invalid".format((correct+incorrect), valid, incorrect))
def check_password(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    special_characters = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch in special_characters:
            has_special = True

    if (len(password) >= 8 and has_upper and
            has_lower and has_digit and has_special):
        print("Strong Password")
    else:
        print("Weak Password")


password = input("Enter Password: ")
check_password(password)
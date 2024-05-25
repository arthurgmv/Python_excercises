def format_name():
    f_name = input("What's your first name? ").capitalize()
    l_name = input("What's your last name? ").capitalize()
    return f_name + " " + l_name


name = format_name()
print(f"Welcome {name}")

input("press enter to finish the programme")

import csv

with open("not_a_database.csv") as open_file:
    contents = list(csv.DictReader(open_file))


def login(contents):
    while True:
        print ("Login")
        username = input("Username?\n>")
        password = input("Password?\n>")
        for line in contents:
            if username == line["username"] and password == line["password"]:
                return False
            else:
                continue


def logged_in(contents):
    print ("What would you like to do?")
    choice = input("[A]dd a new user?\n[L]ogout?")
    if choice == "A" or choice == "a":
        username = input("Pick a username\n>")
        # for line in contents:
        #     if username == line["username"]:
        #         print ("This username is not available")
        #     else:
        #         break
        password = input("Pick a password\n>")
        fullname = input("What is your full name?\n>")
        facts = input("What is a short fact about yourself?\n>")
        with open("not_a_database.csv", "a") as open_file:
            headers = ["username", "password", "full name", "facts"]
            write_contents = csv.DictWriter(open_file, fieldnames=headers)
            write_contents.writerow({"username": "{}".format(username), "password": "{}".format(password),
                                     "full name": "{}".format(fullname), "facts": "{}".format(facts)})
    elif choice == "L" or choice == "l":
        login(contents)
    else:
        print ("Invalid response")
        logged_in(contents)

if login(contents) == False:
    logged_in(contents)

import sys
filepath = "Story.txt.txt"
while True:
    print("1. Add New Entry\n2. Read Your Diary\n3. Exit")
    user_input = input("Enter your choice: ").strip().lower()
    match user_input:
        case "3":
            sys.exit(0)
        case "2":
            with open(filepath, 'r') as file:
                file_contents = file.read()
                print(file_contents)
        case "1":
            user_date = input("Enter todays date: ")
            user_entry = input("Enter your entry: ")
            with open(filepath, 'a+') as file:
                file.read()
                file_entry = file.write(user_date + "\n" + user_entry)
        case _:
            print("Invalid Input")
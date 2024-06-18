print()
user_name = input("Hello, I'm Sandra, your virtual assistant. I will help you organize your daily tasks. Please tell me your name: ").capitalize()
print()
print(user_name + ", Nice to meet you!", end=" ")

from datetime import datetime
today = datetime.today()
print("Today is", today, " and here are some suggestions to keep you active:")

menu = ["Call a friend", "Finish Coding Project", "Go to the gym", "Go to the grocery store", "Cook dinner", "Go to bed early", "Go to the library", "File Taxes", 
        "Play games", "Win Souls", "Go to church", "Write an email", "Watch a Movie", "Read a book"]
print()
menu_enum = enumerate(menu)
for i, item in menu_enum:
    print(i, item)
    
def user_choices(menu):
    tasks = []
    print()
    while True:
        user_selection = input("Please enter the task you would like to do today: ")
        #tried: str(int(input("Please enter the number for the task you would like to do today: ")))
        #tried: int(input("Please enter the number for the task you would like to do today: "))
        if user_selection in menu:
        #tried: if user_selection >= 0 and user_selection <= len(menu) + 1:
            print()
            print("You have chosen to", user_selection, "today, I will remind you to", tasks.append(user_selection), "later.")
        else:
            print("Invalid input. Please try again.")
            continue
        user_add = input("Would you like to add another task? (yes/no)")
        if user_add == "yes":
            print()
            user_more = input("Please enter the task you would like to add: ")
            #tried: str(int(input("Please enter the number for the task you would like to do today: ")))
            #tried: int(input("Please enter the number for the task you would like to do today: "))
            # if user_more in range(1, len(menu) + 1):
            if user_more in menu:
                tasks.append(user_more)
                print()
                print("You have chosen to add", tasks.append(user_more), " to your activities today, I will remind you. ")
            else:
                print("Invalid input. Please try again.")
                continue
        elif user_add == "no":
                print()
                print("Ok. I will remind you to: ")
                for task in tasks:
                    print("-" + task)
                    print()
                print("Have a great day!")
                break
        else:
            print("Invalid input. Please try again.")


user_choices(menu)
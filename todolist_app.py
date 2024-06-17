print()
user_name = input("Hello, I'm Sandra, your virtual assistant. I will help you organize your daily tasks. Please tell me your name:   ").capitalize()
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
    print()
    while True:
        user_selection = int(input("Please enter the number for the task you would like to do today: "))
        if user_selection in range(1, len(menu) + 1):
            print()
            print("You have chosen to", menu[user_selection], "today, I will remind you to do this task. ")
        user_add = input("Would you like to add another task? (yes/no)")
        if user_add == "yes":
            print()
            user_more = int(input("Please enter the number for the task you would like to add: "))
            if user_more in range(1, len(menu) + 1):
                menu[user_selection] = menu[user_selection] + " and " + menu[user_more]
                print("You have chosen to add", menu[user_selection], " to your activities today, I will remind you. ") 
        elif user_add == "no":
            print("Ok. I will remind you to", menu[user_selection], ".")
            break
        else:
             if user_more not in range(1, len(menu) + 1):
                print("Invalid input. Please try again.")
        
        
     





user_choices(menu)
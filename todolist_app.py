#Git Repository:https://github.com/EngineerStephen/todolist_app.git


print()
user_name = input("Hello, I'm Sandra, your virtual assistant. I will help you organize your daily tasks. Please tell me your name: ").capitalize()
print()
print(user_name + ", Nice to meet you!", end=" ")

from datetime import datetime
today = datetime.today()
print("Today is", today, " and here are some suggestions to keep you active:")

menu = ["call a friend", "finish coding project", "go to the gym", "go to the grocery store", "cook dinner", "go to bed early", "go to the library", "file taxes", 
        "play games", "win souls", "go to church", "write an email", "watch a movie", "read a book"]
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
        if user_selection in menu: #tried: if user_selection >= 0 and user_selection <= len(menu) + 1:
            print()
            print( "Okay, I will remind you to", user_selection, "today.")
        else:
            print("Invalid input. Please try again.")
        user_add = input("Would you like to add another task? (yes/no)")
        if user_add == "yes":
            print()
            user_more = input("Please enter another task you would like to add: ")
                #tried: str(int(input("Please enter the number for the task you would like to do today: ")))
                #tried: int(input("Please enter the number for the task you would like to do today: "))
                # if user_more in range(1, len(menu) + 1):
            if user_more in menu:
                tasks.append(user_more)
                print()
                print(user_more, " has been added to your activities today, I will remind you. ")
            else:
                    print("Invalid input. Please try again.")
        elif user_add == "no":
            print()
            print("Ok. I will remind you to: ")
            for task in tasks:
                    print("-" + task)
                    print()
        user_remove = input("Would you like to remove a task? (yes/no)")
        if user_remove == "yes":
            print()
            user_less = input("Please enter the task you would like to remove: ")
            if user_less in tasks:
                tasks.remove(user_less)
                print()
                print(tasks.remove(user_less), " has been removed from your activities today, I will NOT remind you. ")
        elif user_remove == "no":
            print()
            print("Ok")
            for task in tasks:
                print("-" + task)
                print()
        else:
            print("Invalid input. Please try again.")
            print()
        user_quit = input("Would you like to quit the application? (yes/no)")
        if user_quit == "yes":
            print()
            print("Thank you for using the To-Do List App, Have a great day!.")
            print(tasks)
            break
        elif user_quit == "no":
            continue
        else:
            print("Invalid input. Please try again.")


user_choices(menu)



#next steps:
# # Organize your code into functions to promote modularity and readability
# If you feel adventurous, you can add extra features like task priorities, due dates, or color-coding tasks based on their status
# Implement the following features for the To-Do List:
# Adding a task.
# # Marking a task as complete. (Bonus) (Hint: Use string manipulation to add "X" to the end of a task)
# Deleting a task.
# Quitting the application.
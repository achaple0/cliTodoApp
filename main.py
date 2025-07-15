todo_list = []

running = True

def add_list_item(item):
    todo_list.append(item)

def delete_list_item(item):
     del todo_list[item]

def view_list_item():
    for index, item in enumerate(todo_list):
        print(f"{index + 1}. {item}")

# def update_list_item(): 
#     return 

while running: 
    user_selection = input("What would you like to do? ")
    user_selection = user_selection.lower()

    if user_selection == "add":
        item = input("Enter your todo item: ")
        add_list_item(item)
    elif user_selection == "delete":
        item = input("Which item would you like to delete? Please enter the item number: ")
        item = int(item)
        item -= 1
        if item >= int(len(todo_list)):
            print("The item number you selected is greater than the length of the list that currently exists.")
        for index, items in enumerate(todo_list):
            if item == index:
                delete_list_item(index)
                view_list_item()
    elif user_selection == "view":
        view_list_item()
    elif user_selection == "exit":
        exit()

        

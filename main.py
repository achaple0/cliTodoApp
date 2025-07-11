todo_list = [""]

running = True

def add_list_item(item):
    todo_list.append(item)

def delete_list_item(item):
     del todo_list[item]


# def update_list_item(): 
#     return 

while running: 
    user_selection = input("What would you like to do? ")

    if user_selection == "add":
        item = input("Enter your todo item: ")
        add_list_item(item)
        print(todo_list)
    if user_selection == "delete":
        item = input("Which item would you like to delete? Please enter the item number: ")
        if item:
            item = item.enumerate()
            delete_list_item(item)
        print(todo_list)

    
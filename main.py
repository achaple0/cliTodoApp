import string

# Init list
todo_list = []

# Functions that will be called inside loop to handle user input
def add_list_item(item):
    todo_list.append(item)

def delete_list_item(item):
    del todo_list[item]

def view_list_item():
    for index, item in enumerate(todo_list):
        print(f"{index + 1}. {item}")

def update_list_item(item, updated_item): 
    todo_list[item - 1] = updated_item

# setting running variable to true, this will keep from exiting
running = True

while running: 
    user_selection = input("What would you like to do? ")
    
    # modifying input to avoid code breaking
    user_selection = user_selection.lower()
    user_selection = user_selection.strip()
    user_selection = user_selection.translate(str.maketrans('', '', string.punctuation))
    
    # User selection coniditional handler
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

    elif user_selection == "update":
        item = input("Enter the number of the item you want to update: ")
        item = int(item)
        updated_item = input("What would like to replace this item with? ")
        update_list_item(item, updated_item)

    elif user_selection == "view":
        view_list_item()

    elif user_selection == "exit":
        exit()

        

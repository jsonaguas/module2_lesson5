items = []

def add_items():
    new_item = input("Enter item: ")
    if new_item == "":
        print("You cannot add an empty item")
        return
    items.append(new_item)
    print(f"You have added: {new_item}")
    return items
    

def display_items(items):
    for item in items:
        print(item)

def delete_items(items):
    display_items(items)
    item_to_delete = input("Enter item to delete: ")
    items.remove(item_to_delete)
    print(f"You have deleted: {item_to_delete}")
    return items

while True:
    user_prompt = input('''Hi! What would you like to do?"
                        1. Add item
                        2. Display items
                        3. Delete item
                        4. Exit
                        ''')
    if user_prompt == "1":
        add_items()
    elif user_prompt == "2":
        display_items(items)
    elif user_prompt == "3":
        delete_items(items)
    elif user_prompt == "4":
        break





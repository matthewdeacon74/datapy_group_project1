import datetime
import inventory  # Only used in function calls, not function defs


def display_all(inventory: list):
    for item in inventory:
        print()  # blank line between books
        print(f"Title: {item.title}")
        print(f"Author: {item.author}")
        print(f"Status: {item.status}")
        print(f"Condition: {item.condition}%")
        print(f"Due Date: {item.due_date}")


def search_by_author(inventory: list):
    find_author = input("Which author do you wish to search for? ")
    search_results = []
    for item in inventory:
        if find_author.lower() in item.author.lower():
            search_results.append(item)
    print(f"Books by {find_author}:")
    for item in search_results:
        print()  # blank line between books
        print(f"Title: {item.title}")
        print(f"Author: {item.author}")
        print(f"Status: {item.status}")
        print(f"Condition: {item.condition}%")
        print(f"Due Date: {item.due_date}")


def search_by_title(inventory: list):
    find_title = input("Which title do you wish to search for? ")
    found = False
    for item in inventory:
        if item.title.lower() == find_title.lower():
            print(f"Title: {item.title}")
            print(f"Author: {item.author}")
            print(f"Status: {item.status}")
            print(f"Condition: {item.condition}%")
            print(f"Due Date: {item.due_date}")
            found = True
            break
    if not found:
        print("I'm sorry, we don't have that one.")


def checkout(inventory: list):
    while True:
        for i, item in enumerate(inventory):
            print(f"{i+1}. {item.title} by {item.author}")
        checkout_book = int(input(f"Which book do you wish to check out (1-{len(inventory)})? "))
        if inventory[checkout_book-1].status == 'checked out':
            print("That book is already checked out, please select another")
        else:
            this_book = inventory[checkout_book-1]
            # check it out and update due date, break the loop
            this_book.status = 'checked out'
            new_due = datetime.date.today() + datetime.timedelta(days=14)
            this_book.due_date = new_due
            print(f"{this_book.title} by {this_book.author} has been checked out.  Please return it by {new_due}.")
            break


# display_all(inventory.inventory)
# search_by_author(inventory.inventory)
# search_by_title(inventory.inventory)
# checkout(inventory.inventory)

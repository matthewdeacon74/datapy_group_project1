import datetime
import inventory  # Only used in function calls, not function defs


def display_all(inventory: list):
    for item in inventory:
        print()  # blank line between books
        print(item.get_inventory())


def search_by_author(inventory: list):
    find_author = input("Which author/director do you wish to search for? ")
    search_results = []
    for item in inventory:
        if hasattr(item, 'author') and find_author.lower() in item.author.lower():
            search_results.append(item)
        if hasattr(item, 'director') and find_author.lower() in item.director.lower():
            search_results.append(item)

    print(f"Books or Movies by {find_author}:")
    for item in search_results:
        print()  # blank line between books
        print(item.get_inventory())


def search_by_title(inventory: list):
    find_title = input("Which title do you wish to search for? ")
    found = False
    for item in inventory:
        if item.title.lower() == find_title.lower():
            print(item.get_inventory())
            found = True
            break
    if not found:
        print("I'm sorry, we don't have that one.")


def checkout(inventory: list):
    while True:
        for i, item in enumerate(inventory):
            if hasattr(item, 'author'):
                print(f"{i+1}. {item.title} by {item.author}")
            if hasattr(item, 'director'):
                print(f"{i+1}. {item.title} directed by {item.director}")
        checkout_book = int(input(f"Which book do you wish to check out (1-{len(inventory)})? "))
        if inventory[checkout_book-1].status == 'out':
            print("That book is already checked out, please select another:")
            print()
        else:
            this_book = inventory[checkout_book-1]
            # check it out and update due date, break the loop
            this_book.status = 'out'
            this_book.condition -= 10
            new_due = datetime.date.today() + datetime.timedelta(days=14)
            this_book.due_date = new_due
            print(f"{this_book.title} by {this_book.author} has been checked out.  Please return it by {new_due}.")
            break


def checkin(inventory:list):
    listnum = 0
    return_stack = []
    out_list = []
    for i, item in enumerate(inventory):
        # build list of only books that are out
        if item.status == 'out':
            if hasattr(item, 'author'):
                author = item.author
            if hasattr(item, 'director'):
                author = item.director
            print(f"{listnum + 1}. {item.title} by {author}")
            out_list.append(inventory[i])
            listnum += 1
    if listnum > 0:
        process_return = 'n'
        while len(return_stack) < listnum and not process_return == 'y':
            user_pick = int(input(f"Which book do you wish to check in (1-{listnum}) or 0 for none? "))
            if user_pick == 0:
                break
            return_stack.append(out_list[user_pick-1])
            print(f"{out_list[user_pick-1].title} has been added to the returns pile")
            process_return = input("Do you wish to process the returns now (y/n)?")
        # process returns
        if process_return == 'y':
            for book in return_stack:
                if book.condition < 20:
                    print(f"{book.title} is no longer usable; it will be removed from circulation and recycled.")
                    print(len(inventory))
                    inventory.remove(book)
                    print(len(inventory))
                else:
                    print(f"{book.title} has been checked in.")
                    print(inventory.index(book))
                    if inventory.index(book) < 0:
                        inventory.append(book)
                    book.status = 'in'
                    book.due_date = 'N/A'
            # exit function
            return
    else:
        print("There aren't any books checked out right now.")

# display_all(inventory.inventory)
# search_by_author(inventory.inventory)
# search_by_title(inventory.inventory)
# checkout(inventory.inventory)
# checkin(inventory.inventory)

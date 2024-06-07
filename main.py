import functions
import inventory


def main():
    while True:
        # Selecting an action (search will result in another selection)
        user_action = input("Welcome to the Detroit Library, what would you like to do?\n"
                            "1. See Inventory\n"
                            "2. Search\n"
                            "3. Check out a book\n"
                            "4. Return a book\n"
                            ">> ")

        while True:

            if user_action == '1' or user_action.lower() in 'see inventory':
                print()
                print("Here are all the books we have at the Detroit Library")
                functions.display_all(inventory.inventory)
                break
            elif user_action == '2' or user_action.lower() in 'search':
                # lets user select either author or title after selecting search
                search_by = input("Would you like to search by author/direct or title? >> ").lower()
                while True:
                    if 'author' in search_by or 'director' in search_by:
                        functions.search_by_author(inventory.inventory)
                        break

                    elif 'title' in search_by:
                        functions.search_by_title(inventory.inventory)
                        break

                    else:
                        search_by = input("Please select either author or title >> ")
                break

            elif user_action == '3' or user_action.lower() in 'check out':
                functions.checkout(inventory.inventory)
                break

            elif user_action == '4' or user_action.lower() in 'return':
                functions.checkin(inventory.inventory)

            else:
                user_action = input("Please select a valid option: ")

        user_continue = input("Would you like to select another action? y or n >> ")
        if user_continue != 'y':
            break

    print()
    print("Thank you, please come again soon!")


if __name__ == '__main__':
    main()

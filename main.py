import functions
import inventory
from media_class import Media, Book, Movie


def main():
    while True:
        # Selecting an action (search will result in another selection)
        user_action = input("Welcome to the Detroit Library, what would you like to do?\n"
                            "1. See Inventory\n"
                            "2. Search\n"
                            "3. Check out a book or movie\n"
                            "4. Return a book or movie\n"
                            "5. Donate a book or movie to the library\n"
                            ">> ")

        while True:

            if user_action == '1' or user_action.lower() in 'see inventory':
                print()
                print("Here are all the books we have at the Detroit Library")
                functions.display_all(inventory.inventory)
                break
            elif user_action == '2' or user_action.lower() in 'search':
                # lets user select either author or title after selecting search
                print()
                search_by = input("Would you like to search by author/director or title? >> ").lower()
                while True:
                    if 'auth' in search_by or 'direct' in search_by:
                        functions.search_by_author(inventory.inventory)
                        break

                    elif 'title' in search_by:
                        functions.search_by_title(inventory.inventory)
                        break

                    else:
                        search_by = input("Please select either author or title >> ")
                break

            elif user_action == '3' or user_action.lower() in 'check out':
                print()
                functions.checkout(inventory.inventory)
                break

            elif user_action == '4' or user_action.lower() in 'return':
                print()
                functions.checkin(inventory.inventory)
                break

            elif user_action == '5' or user_action.lower() in 'donate':
                print()
                while True:
                    donation_type = input("Would you like to donate a book or a movie? ").lower()
                    if donation_type == 'book':
                        user_title = input("What is the name of the book? ")
                        user_author = input(f"Who is the author of {user_title}? ")
                        inventory.inventory.append(Book(user_title, user_author, 'in', 100))
                        break
                    elif donation_type == 'movie':
                        user_title = input("What is the name of the movie? ")
                        user_director = input(f"Who is the director of {user_title}? ")
                        user_runtime = int(input(f"How many minutes long is {user_title}? "))
                        inventory.inventory.append(Movie(user_title, user_director, 'in', 100, user_runtime))
                        break
                    else:
                        print("Please enter a valid option.")
                print(f"Thank you for your {donation_type} donation.")
                print("The following has been added to our inventory and is available to checkout:\n")
                print((inventory.inventory[-1]).get_inventory())
                break

            else:
                user_action = input("Please select a valid option: ")

        print()
        user_continue = input("Would you like to select another action? y or n >> ")
        if user_continue == 'y':
            print()
        else:
            break

    print()
    print("Thank you, please come again soon!")


if __name__ == '__main__':
    main()

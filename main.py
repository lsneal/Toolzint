import github
import location

def display_menu():
    print("==== Menu ====")
    print("[1] Github search mail")
    print("[2] IP info")
    print("[3] Option 3")
    print("[4] Exit")
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        print("You chose Option 1.")
        github.github_search()
    elif choice == '2':
        print("You chose Option 2.")
        location.get_ip_info()
    elif choice == '3':
        print("You chose Option 3.")
    elif choice == '4':
        print("Goodbye!")
        return False
    else:
        print("Invalid option. Try again.")
    
    return True

def menu():
    continue_menu = True
    while continue_menu:
        continue_menu = display_menu()

if __name__ == "__main__":
    menu()
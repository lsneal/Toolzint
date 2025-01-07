import github
import location
import emailpwn

def display_menu():
    print("==== Menu ====")
    print("[1] Github search mail")
    print("[2] IP info")
    print("[3] Check leak email")
    print("[4] Check leak password")
    print("[5] Activate TOR proxy")
    print("[6] Activate pool proxy")
    print("[7] Traffic Obfuscator")
    print("[8] Check DNS leak\n")
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        print("You chose Option 1.")
        github.github_search()
    elif choice == '2':
        print("You chose Option 2.")
        location.get_ip_info()
    elif choice == '3':
        print("You chose Option 3.")
        emailpwn.check_email_pwned()
    elif choice == '4':
        print("You chose Option 4.")
    elif choice == '5':
        print("You chose Option 5.")
    elif choice == '6':
        print("You chose Option 6.")
    elif choice == '7':
        print("You chose Option 7.")
    elif choice == '8':
        print("You chose Option 8")
    else:
        print("Invalid option. Try again.")
    
    return True

def menu():
    continue_menu = True
    while continue_menu:
        continue_menu = display_menu()

if __name__ == "__main__":
    menu()
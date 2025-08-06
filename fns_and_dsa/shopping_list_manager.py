def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add=input("Enter the item to add: ")
            shopping_list.append(add)
            print("Item added to the shopping list.")
            # Prompt for and add an item
            pass
        elif choice == '2':
            rm = input("Enter the item to remove: ")
            if rm in shopping_list: 
                shopping_list.remove(rm)  
                print("Item removed from the shopping list.")
            else:
                print("Item not found in the list.")

            # Prompt for and remove an item
            pass
        elif choice == '3':
            if len(shopping_list)==0:
                print("The shopping list is empty.")
            else:
                    print("Shopping List:")
                    for j in shopping_list:
                        print(j)
            # Display the shopping list
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

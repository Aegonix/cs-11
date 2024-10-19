
#? WAP that displays options for inserting or deleting elements in the list.
#? If the user chooses a delete option, display a submenu and ask if the element is to be deleted with:
#* value or
#* position or
#* a list slice is to be deleted

l: list[str] = []

while True:
    option = input("""-----------------------------------------
Options:
(1) Insert element to the list
(2) Delete an element/slice from the list
(3) Exit
(Enter any number): """)
    print("-----------------------------------------\n")
    
    if option == "1":
        l += [input("Enter element to insert: ")]
        print("The list is now:", l)
        print()

    elif option == "2":
        delete_option = input("""------------------------------------------------
How would you like to delete? (enter any number)
(1) Remove all occurences of a value
(2) Remove by index/position
(3) Remove a slice of the list
(4) Return to original options
(Enter any number): """)
        print("------------------------------------------------\n")

        if delete_option == "1":
            print("Currently, the list is:", l)
            to_remove = input("Enter value to remove: ")
            removed_list: list[str] = []

            for i in l:
                if i != to_remove:
                    removed_list.append(i)

            l = removed_list
            print("The list is now:", l)
            print()

        elif delete_option == "2":
            print("Currently, the list is:", l)
            index = int(input("Enter index to remove: "))
            removed_list: list[str] = []
            x = 0

            for i in range(len(l)):
                if x != index:
                    removed_list.append(l[i])
                
                x += 1

            l = removed_list
            print("The list is now:", l)
            print()

        elif delete_option == "3":
            print("Currently, the list is:", l)
            start = int(input("Enter start index of slice: "))
            end = int(input("Enter end index of slice (non-inclusive): "))

            l = l[:start] + l[end:]
            print("The list is now:", l)
            print()

        elif delete_option == "4":
            pass
        
        else:
            print("Option not recognized. Returning to original options...")
            print()

    elif option == "3":
        print("Exiting...")
        print()
        break

    else:
        print("Option not recognized. Try again.")
        print()

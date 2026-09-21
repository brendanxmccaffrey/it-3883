# Program Name:         Assignment1.py
# Course:               IT3883/Section W01
# Student Name:         Brendan McCaffrey
# Assignment Number:    Lab1
# Due Date:             09/22/2026
# Purpose:              This program provides a text-based menu that allows the user to append, clear,
#                       and display data stored in an input buffer. The program continues until the user chooses to exit.
# Resources used:       IT 3883 Module 1 Content: Moduel 1-1 -Input-output PowerPoint

# Create an empty string to hold the user's input
input_buffer = ""

# Display a text-based menu with four options, and keep menu open until the user chooses "Exit the program".
while True:
    print("\nMenu")
    print("1. Append data to the input buffer")
    print("2. Clear the input buffer")
    print("3. Display the input buffer")
    print("4. Exit the program")

    # Ask the user to select an option from the menu
    choice = input("Please select an option (1-4): ")

    # Process the user's choice
    if choice == "1":
        # Append data to the input buffer
        data = input("Enter data to append: ")
        input_buffer += data
    elif choice == "2":
        # Clear the input buffer
        input_buffer = ""
    elif choice == "3":
        # Display the input buffer
        print("Input buffer:", input_buffer)
    elif choice == "4":
        # Exit the program
        print("Exiting the program.")
        break
    else:
        # Handle invalid input (E.g., if the user enters a letter or a number outside the range of 1-4)
        print("Invalid option. Please select an option (1-4).")
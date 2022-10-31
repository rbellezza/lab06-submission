def menu():
    print('''Simple Calculator
------------------
0.) Addition
1.) Check Operation History
2.) Exit Program\n''')


# Create a main function to operate the program
def main():
    # Create variable for user input
    user_input = 0

    # Create variables for user to enter numbers
    first_number = 0
    second_number = 0
    result_num = 0

    # Create variable to keep track of operations done
    operations = 0
    operation_history = []

    while user_input != 1:
        menu()
        user_input = input("Select a menu option: ")
        if int(user_input) == 0:
            first_number = int(input("Please enter the first number you would like to add."))
            second_number = int(input("Please enter the second number you would like to add."))
            result_num = first_number + second_number
            operations += 1
            operation_history.append(["Addition", first_number, second_number, result_num])
            print("The result of adding the numbers together is ", result_num)

        elif int(user_input) == 1:
            if operations <= 0:
                print("No valid operations to process!")
            else:
                print("The previous history of operations is the following. Individual operations are put within [].")
                print(operation_history)

        elif int(user_input) == 2:
            print("Thank you for using this calculator. Goodbye!")
            break
            
        else:
            print("Invalid value! Please select a different menu option when prompted.")



main()

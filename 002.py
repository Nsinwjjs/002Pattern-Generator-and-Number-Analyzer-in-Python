# Project: Pattern Generator and Number Analyzer
# Objective: Generate patterns and analyze numbers using Python

print("Welcome to Pattern Generator and Number Analyzer")

# This loop runs until the user chooses to exit
while True:
    print("\nMenu:")
    print("1. Generate Pattern")
    print("2. Analyze Numbers")
    print("3. Exit")

    # Take user choice
    choice = input("Enter your choice: ")

    # OPTION 1: PATTERN GENERATOR
    if choice == "1":
        rows = int(input("Enter number of rows: "))

        # Validation for rows
        if rows <= 0:
            print("Number of rows must be greater than zero")
            continue

        print("\nGenerated Pattern:")
        for i in range(1, rows + 1):
            for j in range(i):
                print("*", end="")
            print()

    # OPTION 2: NUMBER ANALYZER
    elif choice == "2":
        start = int(input("Enter start number: "))
        end = int(input("Enter end number: "))

        # Validation for range
        if end < start:
            print("End number must be greater than start number")
            continue

        total = 0
        print("\nNumber Analysis:")
        for num in range(start, end + 1):
            if num % 2 == 0:
                print(num, "is Even")
            else:
                print(num, "is Odd")
            total = total + num

        print("Sum of all numbers =", total)

    # OPTION 3: EXIT
    elif choice == "3":
        print("Thank you for using the program")
        break

    # INVALID INPUT
    else:
        print("Invalid choice, please try again")
        pass

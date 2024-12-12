#functions
def print_menu():
    print("===============================")
    print("1) sum")
    print("2) subtract")
    print("3) multiply")
    print("4) divide")

print_menu()
option = input("Select the option")

num1 = float(input("Please provide a number "))
num2 = float(input("Please provide a second number "))

# proceed with the logic to calculate the total
if option == "1":
    total = num1 + num2
    print("The total is: " + str(total))

elif option == "2":
    total = num1 - num2
    print("The total is: " + str(total))
    if option == "3":
        total = num1 * num2
        print("The total is: " + str(total))

elif option == "4":
        if num2 == 0:
            print("You are trying to divide by zero")
        else:
            total = num1 / num2
        print("The total is: " + str(total))
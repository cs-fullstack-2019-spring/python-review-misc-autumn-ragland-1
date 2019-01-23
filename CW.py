def main():
    # problem1()
    # problem2()
    bonus1()
    # bonus2()

# Create a function that has a loop that quits with q.
# If the user doesn't enter q, ask them to input another string.
# BONUS: Make sure the code can handle whatever case the User enters the q as (uppercase or lowercase).
def problem1():
    userInput = ""
    while userInput != "q":
        userInput = input("Enter anything\nEnter q to quit\n").lower()
# Write 2 functions: exercise2() and exercise2_helper(num1, num2, num3. operation)
# The function exercise2_helper(num1, num2, num3) should expect 3 numbers, and an operation to perform as a String as parameters.
# The function should support 3 operations:
#
# SUM - Return the sum of the 3 numbers
# PROD - Return the product of the 3 numbers
# AVG - Return the average of the 3 numbers
#
# The operation and the returned value should then be printed out back in the main exercise2() function.
# Return INVALID OPERATION if an operation passed in that isn't supported. HINT: Use switch/case
def problem2():

    def problem2a(num1, num2, num3, operation):
        if operation == "sum":
            print("The sum of " + str(num1) + " " + str(num2) + " and " + str(num3) + " is " + str(num1 + num2 + num3))
        elif operation == "prod":
            print("The product of " + str(num1) + " " + str(num2) + " and " + str(num3) + " is " + str(num1 * num2 * num3))
        elif operation == "avg":
            print("The average of " + str(num1) + " " + str(num2) + " and " + str(num3) + " is " + str((num1 + num2 + num3)//3))
        else:
            print("INVALID OPERATION")
    problem2a(2, 4, 6, "sum")
# Write a function that prompts the User for the number of stars to print.
# Then use a loop to print a number of stars/asterisks starting with 1 and up to the number entered by the User.
# If rows is 5, it should print the following:
def bonus1():
    stars = "*"
    userInput = int(input("How many stars do you want to print? "))
    for rows in range(userInput):
        print(stars*(rows+1))

if __name__ == '__main__':
    main()
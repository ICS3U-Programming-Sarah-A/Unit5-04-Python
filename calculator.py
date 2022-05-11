#!/usr/bin/env python3

# Created by: Sarah
# Created on: May 11th, 2022.
# This program asks the user to enter a two numbers and the operation they'd
# like to perform. After asking, it completes the calculation if the responses
# are valid & displays it to the user.


def calculate(sign, first_number, second_number):
    # checks to see if user input corresponds with the following signs.
    if sign == "+":
        results = first_number + second_number
    elif sign == "-":
        results = first_number - second_number
    elif sign == "/":
        results = first_number / second_number
    elif sign == "%":
        results = first_number % second_number
    elif sign == "*":
        results = first_number * second_number
    return results


def main():
    print("This program will perform the calculations between two numbers.")
    print("")

    # get user input from user
    user_sign = input("Enter the operation you'd to perform (+, -, *, /, %): ")
    print("")

    # checks to see if user enters valid operation
    if user_sign == "+" or user_sign == "-" or user_sign == "/" \
       or user_sign == "*" or user_sign == "%":

        # get user input as string
        first_num_string = input("Enter the first number: ")

        try:
            # converts from a string to float
            first_num_float = float(first_num_string)

            # gets the second number as string
            second_num_string = input("Enter the second number: ")

            try:
                # converts from string to float
                second_num_float = float(second_num_string)

                # assigns a variable to function call,
                # giving it a returned value.
                user_results = calculate(user_sign,
                                         first_num_float, second_num_float)

                # displays results to user
                print("The results of {} {} {} is {:,.2f}."
                      .format(first_num_float, user_sign,
                              second_num_float, user_results))
                print("")

            # checks for any invalid cases
            except Exception:
                print("{} is not a valid number.".format(second_num_string))

        # checks for any invalid cases
        except Exception:
            print("{} is not a valid number.".format(first_num_string))

    else:
        print("{} is not one of the following operations.".format(user_sign))


if __name__ == "__main__":
    main()

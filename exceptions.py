# Handling Exceptions, try, except
# Exception types: TypeError, ValueError, IndexError, KeyError, AttributeError, NameError, ZeroDivisionError, FileNotFoundError, ImportError, ModuleNotFoundError, IndentationError, SyntaxError
# runtime errors vs non runtime errors
# SyntaxError occurs at compile time
# runtime error: TypeError, IndexError, KeyError, ValueError


#  KeyError
try:
    a = {"key1": "value"}
    a["access"]
except KeyError:
    print("unvalid")




# IndexError
try:
    makelist = ["with"]
    make[1]
except IndexError:
    print("unvalid")




# ZeroDivisionError exception
while True:
    try:
        10 * (1/0)
        break
    except ZeroDivisionError:
        print("Oops! That was no valid number. Try again..."))

# NameError
while True:
    try:
        4 + spam*3
        break # break goes with while loop only and can be removed
    except NameError:
        print("unvalid")

# TypeError
while True:
    try:
        "2" + 2
        break
    except TypeError:
        print("unvalid")

#
try:
    a = "2"
    b = 2
    c = a + b
except TypeError:
    print("unvalid")

#
try:
    a = []
    b = 2
    c = a + b
except TypeError:
    print("unvalid")

#
try:
    a = {"a": "b"}
    b = a + 1
except TypeError:
    print("unvalid")




# handling exception
while True:
    try:
        a = int(input("Enter an integer")) # the try block functions with more than one variable between
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again..."))






while True:
# show an error message when the user doesnt enter an integer
    try:
        age = int(input("What is your age? "))
    except ValueError:
        print(ValueError)
    else:
        print(f"You are {age} years old!")
        break


# print built-in error
while True:
    try:
        age = int(input("What is your age?" ))
    except ValueError as e:
        print(e)
    else:
        print(f"You are {age} years old!")
        break

# raising an error and changing the message
while True:
    try:
        age = int(input("What is your age? "))
        if age <= 0:
            raise ValueError("That age is invalid. Try again")
    except ValueError as err:
        print(f"{err}")
    else:
        print(f"You are {age} years old!")
        break

# raising error with emptiness
while True
    try:
        weapon = input("Enter a weapon")
        if weapon == "":
            raise ValueError("Try again with an input.")
    except ValueError as err:
        print(f"{err}")
    else:
        print(f"{weapon}")
        break

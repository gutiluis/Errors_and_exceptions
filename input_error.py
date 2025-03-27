try:
    # the input must be an integer
    a = input("Enter a string: ")
    int(a)
except ValueError as err:
    print(f"{err}")

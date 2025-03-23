# run time exceptions

# Import Error
try:
    import some_module
except ImportError:
    print(ImportError)

# AttributeError
try:
    a = str("ing")
    a.append("value")
except AttributeError:
    print("invalid attribute")


# KeyError
try:
    a = {"machine": "attack"}
    a["access"]
except KeyError:
    print(KeyError)


# IndexError
try:
    makelist = ["IndexError"]
    makelist[2]
except IndexError:
    print(IndexError)


# ZeroDivisionError
try:
    2/0
except ZeroDivisionError:
    print(ZeroDivisionError)

#NameError
def x()
    try:
        f
    except NameError:
        print(NameError)


x()

# TypeError
def x():
    try:
        a = ["a_list"]
        b = "value"
        a.__add__(b)
    except TypeError:
        print(TypeError)


(x)

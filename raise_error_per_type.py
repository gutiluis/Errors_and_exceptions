#IndexError
a = [1, 2, 3, 4, 5]
try:
    a[8]
except IndexError:
    print(f"Index out of range. Available range: 0 - {len(a) - 1}")

a = "string for index out of range"
try:
    a[100]
except IndexError:
    print(f"Index out of range. Available range: 0 - {len(a) - 1}")

x = tuple("of this")
try:
    x[100]
except:
    print(f"Index out of range. Available range: 0 - {len(x) - 1}")

# NameError

# TypeError
try:
    c = Ellipsis
    int(c)
except TypeError as err:
    print(f"{err}")

try:
    c = Ellipsis
    list(c)
except TypeError as err:
    print(f"{err}")

try:
    c = Ellipsis
    set(c)
except TypeError as err:
    print(f"{err}")

try:
    x = set("example")
    c[0:1] # object is not subscriptable
except TypeError as err:
    print(f"{err}")

try:
    a = set("object")
    a[0]
except TypeError as err:
    print(f"{err}")

try:
    c = Ellipsis
    dict(c)
except TypeError as err:
    print(f"{err}")


try:
    a = None
    int(a)
except TypeError as err:
    print(f"{err}")

try:
    a = None
    dict(a)
except TypeError as err:
    print(f"{err}")



try:
    c = frozenset("make")
except TypeError as err:
    print(TypeError)
    print(f"{err}"

try:
    int(set("of this"))
except TypeError as err:
    print(f"{err}")
    print(TypeError)

try:
    int(("tuple", "second value"))
except TypeError as err:
    print(f"show error: {err}")
    print(TypeError)


try:
    int({"d": {"ictionary"})
except TypeError as err:
    print(f"{err}"
    print(TypeError)

try:
    int(dict({"print": "dictionary"}))
except TypeError as err:
    print(f"{err}")

try:
    float({"dict": "ionary"})
except TypeError as err:
    print(f"{err}")

try:
    float(list("of this"))
except TypeError as err:
    print(f"{err}")

try:
    int(["make list"])
except TypeError as err:
    print(f"show: {err}"
    print(TypeError)

try:
    int(list("list"))
except TypeError as err:
    print(f"{err}")

try:
    list(123)
except TypeError as err:
    print(f"{err}")

# KeyError
try:
    a = {"fly": "drone"}
    a["attack"]
except KeyError as err:
    raise err


try:
    a = {"gun": "shoot"}
    a["access"]
except KeyError:
    print(KeyError)


try:
    a = {"gun": "1"}
    a["attack"]
except:
    print(KeyError)
    print("error example")

try:
    b = {"gun": "attack"}
    b[2:2]
except:
    print(KeyError)

try:
    a = {"c": "a"}
    a[0]
except KeyError:
    print(KeyError)



# AttributeError
# with string
try:
    a = "string"
    a.clear() # clear from list type
except:
    print(AttributeError)
    print("error")

try:
    a = "string"
    a.clear()
except AttributeError:
    print("error")



# ValueError
try:
     int("tree") # integer for a string
except:
    print(ValueError)
    print("An error Ocurred")

try:
    int(str("with a string"))
except ValueError as err:
    print(f"{err}")


try:
    int("15.99") # invalid literal for int() with base 10
except ValueError as err: # err is a variable
    print(f"an error: {err}")


try:
    float("string")
except ValueError as err:
    print(f"{err}")
    print(ValueError)




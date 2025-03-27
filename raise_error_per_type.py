# NameError

# TypeError

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
    int("15.99")
except ValueError as err: # err is a variable
    print(f"an error: {err}")


try:
    float("string")
except ValueError as err:
    print(f"{err}")
    print(ValueError)


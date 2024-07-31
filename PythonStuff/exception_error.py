# Notes
# Error are of two type : syntax Error[parsing errors] and Exceptions[Error detected during execution]
#
#

# [SE] -> Invalid syntax
# while True print("Hello world")
# [Execption] -> ZeroDivisionError: division by zero
# 10 * (1 / 0)
# [Exceptions] -> NameError : name 'spam; is not defined
# 4 + spam * 3
# [Exe] -> TypeError: can only concatenate str not int to str
#'2' + 2
# check for Tracebacks
# Name of the Execptions ==>> Details of the Exceptions

# Handling Exceptions
while True:
    try:
        x = int(input("Enter a number: "))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again.....")

# the issue created in try block matches the except catch block , it prints the message
# in try except block , if no exception occur in try block, it will skip the except block
# if there is a exception in try block , it will executed the except block
# ===========================

try:
    x = 1 + "a"
    print(x)
except (RuntimeError, TypeError, NameError) as e:
    print("Error time!")
    print(e)
    print(type(e))

# multiple execution handling [e is an instance of exceptions , alias used ]

# [https://www.youtube.com/watch?v=EeofY2uWv2M&list=PLXovS_5EZGh7MMmgukUeg8rE8pfean17G&index=4]

# raise keyword -> Artificially generating the error
# try statement may have more than one except clauses [first matching except clause is triggered]

#
import sys

try:
    f = open("file.txt")
    s = f.readline()
    i = int(s.strip())
# except OSError as err:
#     print("OS error:", err)
except ValueError:
    print("could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")

# err -> instance of the exceptiom- FileNotFoundError

# try except else
try:
    x = 1 + 1
except TypeError:
    print("This is a TypeError")
else:
    print("Else is here!!!!")


# else clause is better , try to use
# exceptions in functions
def this_fails():
    x = 1 / 0


try:
    this_fails()
except ZeroDivisionError as err:
    print("Handling run-time error", err)


try:
    # Some code...
    x = x + 1
except ValueError:
    print("A ValueError occurred!")
else:
    print("No errors occurred!")
finally:
    print("Executing the finally block!")


# try:
#     open("database.sqlite")
# except OSError:
#     raise RuntimeError("Unable to handle error")


def add(num1, num2):
    try:
        if isinstance(num1, int) and isinstance(num2, int):
            return num1 + num2
        else:
            raise Exception("Only int value are allowed")
    # except TypeError:
    #     return ("Invalid Number")
    # except NameError:  # inbuilt exceptions
    #     return("Invalid parameter")
    except Exception as e:  # always provides the base exception at the last
        return e


print(add(12, 12))
print(add("a", "b"))
print(add(7, "a"))
print("Execution completed............")

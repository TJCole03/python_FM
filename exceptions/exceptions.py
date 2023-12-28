try:
    x = int(input("Enter a number: "))
except ValueError:
    print("that number was invalid")

#First, the try clause is executed. If no exception occurs, 
# the except clause is skipped and execution of the try statement is finished. 
# If an exception occurs in the try clause, the rest of the clause is skipped. 
# If the exception’s type matches the exception named after the except keyword, 
# then the except clause is executed. If the exception doesn’t match, then the 
# exception is unhandled and execution stops.

# except clause
# can have multiple exceptions, given as a parenthesized tuple

# try: 
#     # code to try
# except: (RuntimeError, TypeError, NameError):
#     # code to run if one of these exceptions is hit

# #try statements can have more than one except clause 

# try: 
#     # code
# except RuntimeError:
#     #code
# except TypeError:
#     # code
# except NameError: 
#     # code 

# FINALLY BLOCK 
# runs after try, except and else
# good for cleanup regardless of whether an exception is thrown

# try:
#     raise KeyboardInterrupt
# finally:
#     print("Goodbye!!")
    

# BEST PRACTICES

# CATCH MORE SPECIFIC ERRORS FIRST

# try: 
#     my_value = 3.14 / 0 
# except ArithmeticError:
#     print("we have general math error")
# except ZeroDivisionError:
#     print("We can't divide by zero")
# prints out 'we have general math error"
# we want to put ZeroDIvisionError over top of the AritheticError block so we 
# can get more information


# dont't catch Exception. don't catch Exception. don't catch exception; it'll catch 
# every type of exception that subclasses the Exception class. 
# Catching BaseException is worse; it'll swallow up every type of exception including 
# KeyboardInterrupt, which causes programs to exit when sending SIGINT


# class MyCustomException(Exception):
#     pass
# raise MyCustomException()

class IncorrectValueError(Exception):
    def __init__(self, value):
        message = f"heya hoya incorrect value of {value}"
        super().__init__(message)
    my_value = 99.999
    if my_value > 100:
        raise IncorrectValueError(my_value)
    else:
        print('words')

# class IncorrectValueError(Exception):
#     def __init__(self, value):
#         message = f"heya hoya incorrect value of {value}"
#         super().__init__(message)
#     my_value = 99999
#     if my_value > 100:
#         raise IncorrectValueError(my_value)
#     else:
#         print('words')

# >>> new_value = 99
# >>> if new_value > 100:
# ...     raise IncorrectValueError(my_value)
# ... else: 
# ...     print('word')
# ... 
# word
# >>> new_value = 999
# >>> if new_value > 100:
# ...     raise IncorrectValueError(my_value)
# ... else:
# ...     print('word')
# ... 
# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
# IncorrectValueError: incorrect value of {value}

class GitHubApiException(Exception):

    def __init__(self, status_code):
        if status_code == 403:
            message = "Rate limit reached. Please wait a minute and try again."
        else:
            message = f"HTTP Status Code was: {status_code}."

        super().__init__(message)

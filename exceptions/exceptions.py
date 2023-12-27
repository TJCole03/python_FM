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



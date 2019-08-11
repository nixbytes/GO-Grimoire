"""
“we define two global variables. We need to tell the interpreter, 
using the keyword global, that inside the function, 
we are referring to a global variable.”

"""

a = 10
b = 20


def my_function():
    global a
    a = 11
    b = 21


my_function()

print(a)
print(b)


"""
Excerpt From: Benjamin Baka. “Python Data Structures and Algorithms.” iBooks. 
"""

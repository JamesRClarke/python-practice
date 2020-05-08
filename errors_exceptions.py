# def func(a, b):
#     print a + b
#
# func("1", 5)


try:
    a = 20
    b = 0
    print a / b
except ZeroDivisionError: # execute code when there is this specified error
    print 'There is a divide by zero error'
finally:
    print 'This is always going to execute no matter what happens'

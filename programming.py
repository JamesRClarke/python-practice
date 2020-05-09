## Functional
def add_ten(x):
    return x + 10

def twice(fn, arg):
    return fn(fn(arg))

print(twice(add_ten, 10))


## Lambdas
def square(x):
    return x ** 2

print square(4)

result = (lambda x: x ** 2 )(30)

print result

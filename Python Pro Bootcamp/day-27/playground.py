def add(*args):
    total = 0
    for n in args:
        total += n
    return total

#print(add(5, 6, 6))
def calculate(n, **kwargs):
    print(kwargs)
    #for key, value in kwargs.items():
    #    print(key)
    #    print(value)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)
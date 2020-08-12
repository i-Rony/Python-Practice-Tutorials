#currying

def curried_f(x, y = None, z = None):
    def f(x, y, z):
        return x ** 3 + y ** 2 + z

    if y is not None and z is not None:
        return f(x, y, z)
    if y is not None:
        return lambda z: f(x, y, z)
    return lambda y, z = None: (
        f(x, y, z) if (y is not None and z is not None)
        else (lambda z: f(x, y, z))
    )

#print(curried_f(2, 3, 4))
g = curried_f(2)
h = g(3)
i = h(4)
print(i)

# Example 01
float("3.8")
help(float)

# Example 02
float(x="3.8")

# Example 03
def incr(x):
    return x + 1

incr(3.8)

incr(x=3.8)

# Example 04
def incr(x, /):
    return x + 1

incr(3.8)

incr(x=3.8)

# Example 05
def greet(name, /, greeting="Hello"):
    return f"{greeting}, {name}"
 
greet("Christopher")

greet("Christopher", greeting="Awesome job")

greet(name="Christopher", greeting="Did it work?")

# Example 06
def to_fahrenheit(*, celsius):
    return 32 + celsius * 9 / 5

to_fahrenheit(40)

to_fahrenheit(celsius=40)

# Example 07
def headline(text, /, border="~", *, width=50):
    return f" {text} ".center(width, border)

headline("Positional-only Arguments")

headline(text="This doesn't work!")

headline("Python 3.8", "=")

headline("Real Python", border=":")

headline("Python", "@", width=38)

headline("Python", "@", 38)
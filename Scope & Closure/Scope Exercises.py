x = 10


def show():
    x = 5
    print("inside:", x)


show()
print("outside:", x)

# the first x is in the global and the other is in the local

# 2
count = 0


def add():
    global count
    count += 1
    print(count)


add()

# 3 the first one is printed the msg "local" by the rule
msg = "Hi"


def outer():
    msg = "Hello"

    def inner():
        print(msg)

    inner()


outer()


# 4) Using nonlocal (5 דק)
# becouse of the rule LEGB and here we have the local first
def counter():
    num = 0

    def add_one():
        nonlocal num
        num += 1
        print(num)

    add_one()


counter()

# 5) Scope Shadowing (5 דק)
name = "Tom"

def greet():
    global name
print("Hi", name)
greet()
print("Bye", name)











# x = "global"
#
# def outer():
#     x = "enclosing"
#     def inner():
#         x = "local"
#         print(x)
#     inner()
# outer()

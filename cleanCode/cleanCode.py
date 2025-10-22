def calculating_speed(rate, etc):
    return rate / (etc * 60)


print("the kilometer is: ", calculating_speed(120, 2))


# 2) Magic Numbers
def area(r):
    PI = 3.14159
    return PI * r * r


print(area(5))


# 3) Duplicated Code
def print_admin_user_or_user(name, age):
    print("User:", name)
    print("Age:", age)


# 4) Long Function
def user_name(name):
    print("User:", name)


def check_age(age):
    if age < 18:
        print("Minor")
    else:
        print("Adult")
    if age >= 65:
        print("Senior")


user_name("yair")
check_age(25)


# 5) Inconsistent Formatting & Poor Readability
def calc(x, y):
    return x + y


print(calc(2, 3))

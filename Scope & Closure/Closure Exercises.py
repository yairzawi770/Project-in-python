# 1) Basic Closure (5 דק)
def make_greeter(name):
    def greet():
        print("Hi", name)

    return greet


say_hi = make_greeter("Dudu")
say_hi()


# 2)  Discount Factory (10 דק)
def discount_factory(percent):
    def apply(price):
        return price - (price * percent / 100)

    return apply


student = discount_factory(10)
vip = discount_factory(25)
print(student(100))
print(vip(100))

# 3) Multiplier Factory (10 דק)
def make_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply
double = make_multiplier(2)
triple = make_multiplier(3)
quadruple = make_multiplier(4)

print(double(5))   # Expected: 10
print(triple(5))   # Expected: 15
print(double(10))  # Expected: 20
print(triple(7))   # Expected: 21
print(quadruple(5))   # Expected: 20

# 4) Game Score Tracker (Global + Closure 15 דק)
total_score = 0
def player(name):
    score = 0
    def add_points(points):
        global total_score
        nonlocal score
        score = points
        total_score += score
        print(f"{name}: {score} points (Total: {total_score})")
    return add_points

alice = player("Alice")
bob = player("Bob")
alice(10)
bob(20)
alice(15)
bob(35)

# 5) Custom Logger (Global + Closure 15 דק)
total_logs = 0
def logger(prefix):
    count = 0
    def log(msg):
        global total_score
        nonlocal count
        count = 0
        print(f"{prefix} [{count} / {total_logs}]: {msg}")
    return log
# Create different loggers
error = logger("ERROR")
# TODO: create another logger called info with prefix “INFO”
# Test loggers
error("File not found")
error("Access denied")
# TODO: use info logger with your own messages



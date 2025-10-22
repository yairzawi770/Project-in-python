# 1
# def greet(username="david"):
#     return f"hello, {username}!"
# print(greet())

# 2
counts = {"a": 1, "b": 2, "c": 3}
listi = {}
for k in counts:
    if counts[k] % 2 == 0:
        listi[k] = counts[k]
print(listi)

# 3
text = "debugging"
print(text + ("!"))

# 4
nums = [1, 2, 3]
for i in range(0, len(nums)):
    print(nums[i])

# 5
config = {"host": "localhost", "port": 5432}
print(config["port"])

# 6
age = "12"
print(int(age) + 5)

# 7
user_input = "12.5"
print(float(user_input))


# 8) ZeroDivisionError – unchecked divisor
def ratio(a, b):
    return a / b


print(ratio(10, 2))

# 9) ImportError / ModuleNotFoundError – misspelled import
import json

print(json.dumps({"ok": True}))


# 10) RecursionError – missing base case
def down(n):
    if n == 0:
        return n
    print(n)
    return down(n - 1)


print(down(5))

# 11) Infinite loop – loop condition never changes
x = 5
while x > 0:
    print(x)
    x -= 1


# 12) Mutable default argument – state “leaks” across calls
def add_item(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket


print(add_item("a"))
print(add_item("b"))

# 13) Late binding in closures – all functions print same value
funcs = []
for i in range(3):
    funcs.append(i)
print(funcs)

# 14) Modifying a list while iterating – skipped elements
items = [1, 2, 3, 4, 5, 6, 7]
odd = []
for x in items:
    if x % 2 == 1:
        odd.append(x)
print(odd)

# 15) Merge Two Sorted Lists
a = [1, 4, 9]
b = [2, 3, 6, 8]
i, j = 0, 0
merged = []
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        merged.append(a[i])
        i += 1
    else:
        merged.append(b[j])
        j += 1
    if len(a) == i:
        merged.append(b[j])
    elif len(b) == i:
        merged.append(a[i])
print(merged)

# 16) Logging misconfiguration – messages don’t appear
import logging
logging.warning("Start")  # Why no output?

# 17) Wrong Loop Variable – “Same value printed!”
j = 0
for i in range(3):
    j += 1
    print(j)

# 18) f-string with missing variable – runtime NameError
f_name = "Avi "
l_name = "cohen"
full_name = f_name + l_name
print(f"User: {full_name}")

# 19) Off-by-one in range – last element never processed
data = [10, 20, 30, 40]
total = 0
for i in range(len(data)):
    total += data[i]
print("Total:", total)  # Why is 40 missing?


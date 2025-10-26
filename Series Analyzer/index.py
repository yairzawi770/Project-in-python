while True:
    numbers = input("enter 3 positive numbers: ")
    space = numbers.split()
    if len(space) < 3:
        print("put 3 numbers")
        continue

    result = []
    for i in space:
        num = float(i)
        if num <= 0:
           print("it is negative number")
        result.append(num)

    print(  "1. Input a new series"
            "3. Display the series (reversed order)"
            "2. Display the series (original order)"
            "4. Display the series (sorted low→high)"
            "5. Display the Max value"
            "6. Display the Min value"
            "7. Display the Average value"
            "8. Display the Number of elements"
            "9. Display the Sum of the series"
            "0. Exit")

    number = int(input("enter number betwen 0-10: "))
    if number == 1:
        numbers = input("input a new series: ")
    elif number == 2:
        print(result)
    elif number == 3:
        print(result[::-1])
    elif number == 4:
        print(sorted(result))
    elif number == 5:
        print(max(result))
    elif number == 6:
        print(min(result))
    elif number == 7:
        print(sum(result) / len(result))
    elif number == 8:
        print(len(result))
    elif number == 9:
        print(sum(result))
    else:
        print("Finish program")
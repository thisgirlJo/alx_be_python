number = int(input("Enter a number to see its multiplication table: "))

for x in range(1,11):
    times = number * x
    print(number, "*", x, "=", times)

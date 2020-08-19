"""Fizzbuzz for loop variant 2"""
for x in range(1, 101):
    OUTPUT = ""
    if x % 3 == 0:
        OUTPUT += "Fizz"
    if x % 5 == 0:
        OUTPUT += "Buzz"

    if OUTPUT == "":
        OUTPUT += str(x)

    print(OUTPUT)

"""Fizzbuzz for loop variant 3"""
for x in range(1, 101):
    OUTPUT = ""
    if x % 3 == 0:
        OUTPUT += "Fizz"
    if x % 5 == 0:
        OUTPUT += "Buzz"

    print(OUTPUT or x)

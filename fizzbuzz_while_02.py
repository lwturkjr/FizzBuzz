"""Fizzbuzz while loop variant 3"""
X = 0
while X < 100:
    X += 1
    OUTPUT = ""
    if X % 3 == 0:
        OUTPUT += "Fizz"
    if X % 5 == 0:
        OUTPUT += "Buzz"

    print(OUTPUT or X)

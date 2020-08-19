"""Fizzbuzz while loop variant 2"""
X = 0
while X < 100:
    X += 1
    OUTPUT = ""
    if X % 3 == 0:
        OUTPUT += "Fizz"
    if X % 5 == 0:
        OUTPUT += "Buzz"
    if OUTPUT == "":
        OUTPUT += str(X)

    print(OUTPUT)

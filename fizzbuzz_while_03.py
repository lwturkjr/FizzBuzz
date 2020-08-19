"""Fizzbuzz while loop variant 4"""
X = 0
while X < 100:
    X += 1
    OUTPUT = "Fizz" if X % 3 == 0 else ""
    OUTPUT += "Buzz" if X % 5 == 0 else ""

    print(X) if OUTPUT == "" else print(OUTPUT)

"""Fizzbuzz while loop variant 4"""
X = 0
while X < 100:
    X += 1
    print("Fizz" * (X % 3 < 1) + (X % 5 < 1) * "Buzz" or X)

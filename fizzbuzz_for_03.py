"""Fizzbuzz for loop variant 4"""
for x in range(1, 101):
    OUTPUT = "Fizz" if x % 3 == 0 else ""
    OUTPUT += "Buzz" if x % 5 == 0 else ""

    print(x) if OUTPUT == "" else print(OUTPUT)
    
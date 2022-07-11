"""
A series of numbers
The next number is found by adding up 2 numbers before it
0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
"""


def fibonacci_of(n):
    if n in {0, 1}:  #base case
        return n
    return fibonacci_of(n - 1) + fibonacci_of(n - 2)  #recursive case


print(fibonacci_of(15))
result = [fibonacci_of(2) in range(15)]
print(result)
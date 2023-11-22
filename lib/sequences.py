#!/usr/bin/env python3

def print_fibonacci(length):
    # Initialize the first two numbers in the Fibonacci sequence
    if length == 0:
        sequence = []
    elif length == 1:
        sequence = [0]
    else:
        sequence = [0, 1]

    # Generate Fibonacci sequence up to the given length
    while len(sequence) < length:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    print(sequence)
   

    pass


print_fibonacci(9)
print_fibonacci(0)
print_fibonacci(1)
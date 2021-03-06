# Uses python3
import sys


def get_fibonacci_last_digit_naive(n):
    """
    Implments efficient algorithm for finding the last digit of nth
    number in Fibonacci sequence

    Args:
    n -- specifies which Fibonacci number to find

    Returns:
    number -- last digit of nth number of Fibonacci sequence
    """

    if n <= 1:
        return n

    # Initialize array to store Fibonacci sequence
    fib_array = []
    for i in range(n):
        fib_array.append(0)

    fib_array[0] = 1
    fib_array[1] = 1
    for i in range(2,n):
        fib_array[i] = (fib_array[i-1] + fib_array[i-2]) % 10

    number = fib_array[n-1]
    return number


print(get_fibonacci_last_digit_naive(3))
print(get_fibonacci_last_digit_naive(331))
print(get_fibonacci_last_digit_naive(327305))
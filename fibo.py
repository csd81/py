"""Sure! Here's a simple and efficient way to calculate Fibonacci numbers in Python without recursion, which is faster and avoids repeated calculations:"""

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

# Example usage:
n = 10
print(f"Fibonacci number {n} is {fibonacci(n)}")
"""
This uses iteration to build up the sequence from the bottom, only keeping track of the last two numbers.

Would you like me to explain it or generate a recursive version?"""
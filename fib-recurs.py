Here's a simple example of solving the Fibonacci sequence recursively in Python:

def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# Example: print first 10 Fibonacci numbers
for i in range(1, 11):
    print(f"fib({i}) = {fib(i)}")

This defines fib(n) as the sum of the two preceding Fibonacci numbers, with the first two defined as 1.

Let me know if you want me to explain or show a more efficient iterative version!
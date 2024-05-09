def fibonacci_of(n):
    if n in {0, 1}: # Base case
        return n
    return fibonacci_of(n - 1) + fibonacci_of(n - 2) # Recursive case
## memoized function by Achilles
def fibonacci_of_mod(n):
    tabulate = [-1] * (n + 1)  # Initialize table for memoization

    def _fibonacci_of(n):
        if tabulate[n] != -1:  # If value is already calculated, return it
            return tabulate[n]

        if n in {0, 1}:  # Base case
            tabulate[n] = n
        else:
            tabulate[n] = _fibonacci_of(n - 1) + _fibonacci_of(n - 2)  # Recursive case

        return tabulate[n]

    return _fibonacci_of(n)  # Call the inner function

print("Fibonacci number 8 from 1st function: " + str(fibonacci_of(8)))
print("Fibonacci number 8 from 2nd function: " + str(fibonacci_of_mod(8)))



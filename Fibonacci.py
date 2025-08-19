def fibonacci(n):
    """
    Compute the n-th Fibonacci number using an iterative approach.

    Parameters:
        n (int): The index of the Fibonacci sequence (must be non-negative).

    Returns:
        int: The n-th Fibonacci number.

    Raises:
        ValueError: If n is a negative integer.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


if __name__ == "__main__":
    t = int(input("Enter the number of test cases (t): "))
    for _ in range(t):
        n = int(input("Enter an integer (n): "))
        print(f"The {n}-th Fibonacci number is: {fibonacci(n)}")

"""
Bisection Method Implementation
     Method to find a root of the given function
    within a specified interval [a, b], using defined tolerances for both x-values (Delta)
    and function values (Epsilon).
"""

def f(x):
    """
    Function:
        f(x) = (x³ + 4x² + 3x + 5) / (2x³ - 9x² + 18x - 2)
    Parameters:
        x (float): Input value
    Returns:
        float: Computed function value
    """
    return (x**3 + 4*x**2 + 3*x + 5) / (2*x**3 - 9*x**2 + 18*x - 2)


def bisection_method(M, a, b, Delta, Epsilon):
    """
    Perform the Bisection Method to find a root of f(x) in [a, b].

    Parameters:
        M (int): Maximum number of iterations
        a (float): Lower bound of the interval
        b (float): Upper bound of the interval
        Delta (float): Tolerance for x-values (interval size)
        Epsilon (float): Tolerance for function values (f(x))

    Returns:
        float: Estimated root of the function, or None if no root is found in range
    """
    fa = f(a)
    fb = f(b)

    # Check if initial interval is valid
    if fa * fb > 0:
        print("No root exists in this range.")
        return None

    for i in range(M - 1):
        print(f"{i:4d} {a:12.4f} {b:12.4f} {fa:12.4e} {fb:12.4e}")

        # Midpoint
        c = (a + b) / 2
        fc = f(c)

        # Stopping conditions
        if abs(fc) < Epsilon or (b - a) / 2 <= Delta:
            return c

        # Narrowing the interval
        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc

    # Return last midpoint if max iterations reached
    return (a + b) / 2


if __name__ == "__main__":
    # User inputs
    M = int(input("Enter maximum number of iterations: "))
    a = float(input("Enter lower limit of your range: "))
    b = float(input("Enter upper limit of your range: "))
    Delta = float(input("Enter tolerance value for the x-values (Delta): "))
    Epsilon = float(input("Enter tolerance value for the function value f(x) (Epsilon): "))


    print("20221006 \t Aatif Mashkoor")

    # Run Bisection Method
    root = bisection_method(M, a, b, Delta, Epsilon)
    if root is not None:
        print(f"Estimated root: {root:.6f}")



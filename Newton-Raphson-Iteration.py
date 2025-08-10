"""
Newton-Raphson Method – Find Roots Like a Pro

We’re solving this equation:
    e^x - 1.5 - atan(x) = 0

The Newton-Raphson method is basically:
    1. Guess a starting point (x0)
    2. Draw the tangent line at that point
    3. See where it crosses the x-axis – that's your new guess
    4. Repeat until it’s “good enough”

Update formula:
    x_(n+1) = x_n - f(x_n) / f'(x_n)

What you need:
    - The function f(x)
    - Its derivative f'(x)
    - A decent starting guess (or you’ll be lost in math space)
"""

import math as mt

# -------------------------------------------------
# The function we want to find the root of
# -------------------------------------------------
def f(x): 
    """
    f(x) = e^x - 1.5 - atan(x)

    Parameters:
        x (float): The current guess

    Returns:
        float: Function value at x
    """
    return mt.exp(x) - 1.5 - mt.atan(x)

# -------------------------------------------------
# Its derivative (because Newton-Raphson needs it)
# -------------------------------------------------
def derivf(x):
    """
    f'(x) = e^x - 1/(1 + x^2)

    Parameters:
        x (float): The current guess

    Returns:
        float: Derivative value at x
    """
    return mt.exp(x) - (1 / (1 + x**2))

# -------------------------------------------------
# Newton-Raphson magic happens here
# -------------------------------------------------
def Newton_Raphson(x, m, delta=1e-18, epsilon=1e-18):
    """
    Newton-Raphson root finder.

    Parameters:
        x (float): Your starting guess
        m (int): How many times to try (max iterations)
        delta (float): How close two guesses have to be before we quit
        epsilon (float): How close f(x) has to be to zero before we quit

    This prints:
        Iteration number, the current guess, and f(x) at that guess
    """
    # Check the starting point
    a = f(x)
    print(0, x, a)

    for i in range(m - 1):
        slope = derivf(x)

        if slope == 0:
            print("Uh oh, slope is zero. Can't continue.")
            break

        # Newton-Raphson update
        x_new = x - a / slope
        a = f(x_new)

        print(i + 1, x_new, a)

        # Quit if we've hit the target accuracy
        if abs(x_new - x) < delta or abs(a) < epsilon:
            print("Nice! We’ve hit the tolerance limit. Stopping.")
            break

        x = x_new

# -------------------------------------------------
# Run an example
# -------------------------------------------------
if __name__ == "__main__":
    # Start from x = 5, try up to 40 steps
    Newton_Raphson(x=5, m=40)

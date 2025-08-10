import math as mt

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

def f(x):
    '''The function for which we want to find the root. f(x) = e^x - sin(x)'''
    return mt.exp(x) - mt.sin(x)

def bisection(a, b, delta, epsilon, max_iter):
    '''
    Finds the root of a function f(x) using the bisection method.

    Parameters:
        a (float): The start of the interval.
        b (float): The end of the interval.
        delta (float): Tolerance for the interval size. The algorithm stops if (b-a) < delta.
        epsilon (float): Tolerance for the function value. The algorithm stops if |f(midpoint)| < epsilon.
        max_iter (int): The maximum number of iterations to perform.
    
    Returns:
        float: The approximate root of the function, or None if not found.
    '''
    # Check if a root is guaranteed in the interval
    if sign(f(a)) == sign(f(b)):
        print("Error: f(a) and f(b) must have opposite signs.")
        return None

    for i in range(max_iter):
     
        midpoint = (a + b) / 2
        f_midpoint = f(midpoint)

        # Check if the interval is small enough or the function value is close to zero.
        if (b - a) < delta or abs(f_midpoint) < epsilon:
            print(f"Root found after {i+1} iterations.")
            return midpoint
        
        # Update the interval
        if sign(f(a)) != sign(f_midpoint):
            b = midpoint
        else:
            a = midpoint

    print(f"Reached max iterations ({max_iter}). Returning best approximation.")
    return (a + b) / 2


root = bisection(a=-4, b=-3, delta=0.001, epsilon=0.001, max_iter=20)

# Check if a root was found before printing
if root is not None:
    print(f"The approximate root is: {root}")
    print(f"The value of f(root) is: {f(root)}")

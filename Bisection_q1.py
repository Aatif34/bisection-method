def f(x):
    # f(x) = (x**3 + 4*x**2 + 3*x + 5) / (2*x**3 - 9*x**2 + 18*x - 2)
    return (x**3 + 4*x**2 + 3*x + 5) / (2*x**3 - 9*x**2 + 18*x - 2)

def bisection_method(M, a, b, Delta, Epsilon):
    fa = f(a)
    fb = f(b)
    
    if fa * fb > 0:
        print("No root exists in this range")
        return None

    print("\nIter      a            b            f(a)          f(b)          c            f(c)")
    for i in range(M):
        c = (a + b)/2
        fc = f(c)

        # Print before updating a or b
        print(f"{i+1:4d} {a:12.6f} {b:12.6f} {fa:12.4e} {fb:12.4e} {c:12.6f} {fc:12.4e}")

        # Check stopping conditions 
        if abs(fc) < Epsilon or (b-a)/2 <= Delta:
            return c
        
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    # If reached M iterations, return last midpoint
    return (a + b) / 2


# ---- Main program ----
M = int(input("Enter how much you want to do iterations: "))
a = float(input("Enter your lower limit of your range: "))
b = float(input("Enter upper limit of your range: "))
Delta = float(input("Enter tolerance value for the x-values: "))
Epsilon = float(input("Enetr tolerance value for the function value f(x): "))

print("\n20221006 \t Aatif Mashkoor\n")

root = bisection_method(M, a, b, Delta, Epsilon)
if root is not None:
    print(f"\nApproximate root = {root:.6f}")



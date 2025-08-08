# Bisection Method Root Finder

A simple and clear Python implementation of the bisection method for finding the root of a mathematical function. This project is intended as a straightforward example of a common numerical analysis algorithm.



---

## 📖 Description

The bisection method is a root-finding algorithm that repeatedly bisects an interval and then selects a sub-interval in which a root must lie for further processing. It's a simple, robust method, guaranteed to converge on a root if the initial conditions are met.

This script is pre-configured to find the root of the function:
$$ f(x) = e^x - \sin(x) $$

---

## 🚀 How to Use

To run this project on your local machine, follow these simple steps.

### Prerequisites

* You need to have **Python 3** installed on your system.
* You need **Git** to clone the repository.

### Installation & Execution

1.  **Clone the repository** to your local machine:
    ```bash
    git clone [https://github.com/Aatif34/bisection-method-solver.git](https://github.com/Aatif34/numerical-methods-py.git)
    ```

2.  **Navigate into the project directory:**
    ```bash
    cd numerical-methods-py
    ```

3.  **Run the script:**
    ```bash
    python main.py
    ```
    The script will print the approximate root and the value of the function at that root.

---

## 🔧 How to Modify the Code

You can easily adapt this script to find the root of a different function.

1.  **Open the `main.py` file** in your favorite code editor.
2.  **Change the function `f(x)`:**
    ```python
    def f(x):
        # Change the line below to your desired function
        return mt.exp(x) - mt.sin(x)
    ```
3.  **Adjust the interval and parameters:**
    Update the values for `a`, `b`, `delta`, `epsilon`, and `max_iter` in the function call at the bottom of the file.
    ```python
    # Update these values for your new function
    root = bisection(a=-4, b=-3, delta=0.001, epsilon=0.001, max_iter=20)
    ```

---

## 📄 License

This project is licensed under the **MIT License**. See the `LICENSE` file for more details. You are free to use, modify, and distribute this code.

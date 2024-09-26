import sympy as sp

# Define the variable for differentiation
x, y = sp.symbols('x y')

# Trigonometric function differentiation
def differentiate_trig_function():
    print("Choose the trigonometric function to differentiate:")
    print("1. sin(x)")
    print("2. cos(x)")
    print("3. tan(x)")
    print("4. cot(x)")
    print("5. sec(x)")
    print("6. csc(x)")
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        func = sp.sin(x)
    elif choice == '2':
        func = sp.cos(x)
    elif choice == '3':
        func = sp.tan(x)
    elif choice == '4':
        func = sp.cot(x)
    elif choice == '5':
        func = sp.sec(x)
    elif choice == '6':
        func = sp.csc(x)
    else:
        print("Invalid choice!")
        return

    derivative = sp.diff(func, x)
    print(f"d({func})/dx = {derivative}")

# Inverse trigonometric function differentiation
def differentiate_inverse_trig_function():
    print("Choose the inverse trigonometric function to differentiate:")
    print("1. arcsin(x)")
    print("2. arccos(x)")
    print("3. arctan(x)")
    print("4. arccot(x)")
    print("5. arcsec(x)")
    print("6. arccsc(x)")
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        func = sp.asin(x)
    elif choice == '2':
        func = sp.acos(x)
    elif choice == '3':
        func = sp.atan(x)
    elif choice == '4':
        func = sp.acot(x)
    elif choice == '5':
        func = sp.asec(x)
    elif choice == '6':
        func = sp.acsc(x)
    else:
        print("Invalid choice!")
        return

    derivative = sp.diff(func, x)
    print(f"d({func})/dx = {derivative}")

# Logarithmic function differentiation
def differentiate_log_function():
    print("Choose the logarithmic function to differentiate:")
    print("1. ln(x)")
    print("2. log(x, base b)")
    choice = input("Enter your choice (1-2): ")

    if choice == '1':
        func = sp.log(x)
        derivative = sp.diff(func, x)
        print(f"d(ln(x))/dx = {derivative}")
    elif choice == '2':
        base = float(input("Enter the base b: "))
        func = sp.log(x, base)
        derivative = sp.diff(func, x)
        print(f"d(log(x, {base}))/dx = {derivative}")
    else:
        print("Invalid choice!")

# Implicit differentiation
def implicit_differentiation():
    equation = input("Enter the equation in terms of x and y (e.g., x**2 + y**2 - 1): ")
    implicit_func = sp.sympify(equation)
    derivative = sp.diff(implicit_func, x).simplify()
    dydx = sp.solve(derivative, sp.Derivative(y, x))[0]
    print(f"The implicit derivative dy/dx is: {dydx}")

# Second-order derivative
def second_order_derivative():
    print("Choose the function to differentiate twice:")
    print("1. sin(x)")
    print("2. cos(x)")
    print("3. tan(x)")
    print("4. ln(x)")
    print("5. log(x)")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        func = sp.sin(x)
    elif choice == '2':
        func = sp.cos(x)
    elif choice == '3':
        func = sp.tan(x)
    elif choice == '4':
        func = sp.log(x)
    elif choice == '5':
        base = float(input("Enter the base for log(x, base): "))
        func = sp.log(x, base)
    else:
        print("Invalid choice!")
        return

    first_derivative = sp.diff(func, x)
    second_derivative = sp.diff(first_derivative, x)
    print(f"The second-order derivative of {func} is: {second_derivative}")

# Main menu
def main():
    while True:
        print("\nSelect an operation:")
        print("1. Differentiate a trigonometric function")
        print("2. Differentiate an inverse trigonometric function")
        print("3. Differentiate a logarithmic function")
        print("4. Implicit differentiation")
        print("5. Second-order derivative")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            differentiate_trig_function()
        elif choice == '2':
            differentiate_inverse_trig_function()
        elif choice == '3':
            differentiate_log_function()
        elif choice == '4':
            implicit_differentiation()
        elif choice == '5':
            second_order_derivative()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please select a valid operation.")

if __name__ == "__main__":
    main()

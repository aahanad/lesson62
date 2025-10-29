print("Choose the type of equation:")
print("1. Linear (y = mx + c)")
print("2. Quadratic (y = ax^2 + bx + c)")
choice = input("Enter 1 or 2: ")
if choice == "1":
    print("\nYou chose a Linear Equation: y = mx + c")
    m = float(input("Enter the value of m (slope): "))
    c = float(input("Enter the value of c (intercept): "))
    print("\nValues of y for x = 0 to 50:")
    for x in range(0, 51):
        y = m * x + c
        print(f"x = {x}, y = {y}")
elif choice == "2":
    print("\nYou chose a Quadratic Equation: y = ax^2 + bx + c")
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    c = float(input("Enter the value of c: "))
    print("\nValues of y for x = 0 to 50:")
    for x in range(0, 51):
        y = a * x**2 + b * x + c
        print(f"x = {x}, y = {y}")
else:
    print("\nInvalid choice! Please restart the program and enter 1 or 2.")

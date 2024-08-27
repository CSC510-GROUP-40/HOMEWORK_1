import math

def solve_quadratic(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Check if the discriminant is positive, zero or negative
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (root1, root2)
    elif discriminant == 0:
        root = -b / (2*a)
        return (root)
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return (root1, root2)


result = solve_quadratic(1, 2, 5)
print(result)
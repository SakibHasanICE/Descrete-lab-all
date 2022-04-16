# Python3 implementation of Bisection
# Method for solving equations

MAX_ITER = 1000000


# An example function whose solution
# is determined using Bisection Method.
# The function is x^3 - x^2 + 2
def func(x):
    return (x * x * x - 2 * x -5)


# Prints root of func(x) in interval [a, b]
def regulaFalsi(a, b):
    if func(a) * func(b) >= 0:
        print("You have not assumed right a and b")
        return -1

    c = a  # Initialize result

    for i in range(MAX_ITER):

        # Find the point that touches x axis
        c = (a * func(b) - b * func(a)) / (func(b) - func(a))

        # Check if the above found point is root
        if func(c) == 0:
            break

        # Decide the side to repeat the steps
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c
    print("The value of root is : ", '%.4f' % c)


# Driver code to test above function
# Initial values assumed
a = -200
b = 300
regulaFalsi(a, b)

# This code is contributed by "Sharad_Bhardwaj".
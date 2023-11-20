from scipy import integrate

# Define the integrand
def integrand(x1, x2):
    return 1

# Set up the integration limits
x2_lower = -1
x2_upper = 1
x1_lower = -1
x1_upper = lambda x2: 1 - x2

# Perform the double integral
area, _ = integrate.dblquad(integrand, x2_lower, x2_upper, x1_lower, x1_upper)

print("Area of the region:", area)

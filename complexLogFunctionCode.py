import math

print("Program for separate Complex Logarithmic Function into real and imaginary parts")

# Taking the input from the User.

x = int(input("Enter the Real Part of the complex Log function:"))

y = int(input("Enter the Imaginary Part of the complex Log function:"))

# displaying the entered Values into Complex Logarithmic Function.

print("The Complex Log Function entered: log(",  x,"+ i", y, ")")

# This Complex Logarithmic function can be solved in the following manner - Using Euler's identity result.
# log(x + iy) = 0.5*(log(x**2 + y**2)) + i(tan^-1(y/x)    ..........eq(1).
# separately solving the above eq(1).

# to obtain Real Part.
real = 0.5 * math.log((x**2 + y**2),10)

# to obtain the Imaginary Part.
ima = math.degrees(math.atan(y/x))

# Displaying these two Parts separately.
print("The Real Part of the complex Log function:", real)
print("The Imaginary Part of the complex Log function: ",ima)

# displaying into eq(1) from.
print("log(",  x ,"+ i", y, ") =",real,"+ i",ima)

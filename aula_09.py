#How to work with and solve math problems
#Working through the input
valueA = int(input("What is the value of A? "))
valueB = int(input("What is the value of B? "))

#To get things faster, create variables for the results of the operations, so we can use them later in the code if needed, instead of doing the operations again. It is more efficient and faster to do it that way.
addition_result = valueA + valueB
subtraction_result = valueA - valueB
multiplication_result = valueA * valueB
division_result = valueA / valueB
modulo_result = valueA % valueB
exponentiation_result = valueA ** valueB

print("Addition: ", addition_result)
print("Subtraction: ", subtraction_result)  
print("Multiplication: ", multiplication_result)
print("Division: ", division_result)
print("Modulo: ", modulo_result)
print("Exponentiation: ", exponentiation_result)

#Or we can do that way, without creating variables for the results, but it is less efficient if we want to use the results later in the code
print("###########################################")
# + Addition
print("Addition: ", valueA + valueB)

# - Subtraction
print("Subtraction: ", valueA - valueB)

# * Multiplication
print("Multiplication: ", valueA * valueB)

# / Division
print("Division: ", valueA / valueB)

#In division, to ignore the decimal part, we can use // to have an integer number as result
print("Division without decimal part: ", valueA // valueB)

# % Modulo (remainder of the division) will always result in an integer number, even if the numbers are float
print("Modulo: ", valueA % valueB)

# ** Exponentiation (power)
print("Exponentiation: ", valueA ** valueB)

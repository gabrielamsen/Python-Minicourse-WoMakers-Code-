#Special operations
#Such as incrementing and decrementing a variable, which is a common operation in programming, especially in loops.

valueA = int(input("What is the value of A? "))
valueB = int(input("What is the value of B? "))
# += Incrementing
valueA += 5
print("A's Final value: ", valueA)

# -= Decrementing
valueB -= 3
print("B's Final value after decrementing: ", valueB)

# % Modulo
# == exactly equal to
# If value A divided by 2 has a remainder of 0, then it is an even number, otherwise it is an odd number. We can use that to check if a number is even or odd.
if valueA % 2 == 0:
    print("A is an even number")
else:    
    print("A is an odd number")
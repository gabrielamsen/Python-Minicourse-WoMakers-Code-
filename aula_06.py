#Integer numbers (whole numbers)
school = 12
classes_taken = 35
students = 50 

print("School code: ", school, "Classes taken: ", classes_taken, "Students: ", students)

#This is not an integer number, it's called float number (decimal number)
price = 2.50

#Now, to turn it into an integer number, we can use the int() function
print("Price per unit: ", int(price))

#Directly in the terminal, we can also use the int() function to convert a float number into an integer number
promotional_price = int(float(input("Promotional price: ")))
print("Promotional price: ", promotional_price)
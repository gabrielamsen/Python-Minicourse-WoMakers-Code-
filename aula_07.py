#Float numbers (decimal numbers)
price = 2.50
print("Price per unit: ", price)

#Now, to turn this float number into an integer number, we are going to use the int() function
print("Price per unit: ", int(price))

#If you want to directly convert a float number into an integer number in the terminal, you can also use the int() function
promotional_price = int(float(input("Promotional price: ")))
print("Promotional price: ", promotional_price)

#To calculate the difference between the original price and the promotional price, we can use the subtraction operator (-)
print("Price difference: ", price - promotional_price)

#Now we are going to calculate the price difference without turning a float number into an integer number
promotional_price = float(input("Promotional price: "))
print("Promotional price: ", promotional_price)
print("Price difference: ", price - promotional_price)

#Putting the price through the terminal
price = float(input("Price per unit: "))
promotional_price = float(input("Promotional price: "))
print("Price difference: ", (round(price - promotional_price, 2 )))


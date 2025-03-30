# Greet the user to the pizza ordering machine
print("Welcome to the pizza ordering machine!")
print("Please enter the number of pizzas you would like to order.")
# Get the number of pizzas the user wants to order

# Check the user input and make sure the input is provided in the correct format
while True:
    try:
        num_pizzas = int(input("Please enter the number of pizzas you would like to order: "))
        num_pizzas = int(num_pizzas)
        break
    except ValueError:
        print("Please enter a valid number.")
        

# Make sure the user has entered a valid number of pizzas
while num_pizzas <= 0:
    print("Please enter a valid number of pizzas.")
    num_pizzas = int(input("Please enter the number of pizzas you would like to order: "))

# Get the size of the pizzas the user wants to order
print("Please enter the size of the pizzas you would like to order.")
print("1. Small")
print("2. Medium")
print("3. Large")


available_Size = {"Small", "Medium", "Large"}

# Check the user input and make sure the input is provided as per the provided options
Total = 0
while True:
    selected_size = input("Please enter the size of the pizzas you would like to order: ").title()
    if selected_size in available_Size:
        if selected_size == "Small":
            print("You have selected Small size pizza.")
            Total = num_pizzas * 10
            break
        elif selected_size == "Medium":
            print("You have selected Medium size pizza.")
            Total = num_pizzas * 15
            break
        elif selected_size == "Large":
            print("You have selected Large size pizza.")
            Total = num_pizzas * 20
            break
        else:
            print("Please enter a valid size.")
    else:
        print("Please enter a valid size.")

# Get the toppings the user wants to add to the pizzas
print("Please enter the toppings you would like to add to the pizzas.")
Toppings = {"Pepperoni", "Mushrooms", "Onions", "Sausage", "Bacon", "Extra cheese"}
print("1. Pepperoni\n 2. Mushrooms\n 3. Onions\n 4. Sausage\n 5. Bacon\n 6. Extra cheese\n 7. None")

while True:
    selected_topping = input("Please enter the toppings you would like to add to the pizzas: ").title()
    if selected_topping in Toppings:
        if selected_topping == "Pepperoni":
            print("You have selected Pepperoni as a topping.")
            Total += 2
        elif selected_topping == "Mushrooms":
            print("You have selected Mushrooms as a topping.")
            Total += 1
        elif selected_topping == "Onions":
            print("You have selected Onions as a topping.")
            Total += 1
        elif selected_topping == "Sausage":
            print("You have selected Sausage as a topping.")
            Total += 2
        elif selected_topping == "Bacon":
            print("You have selected Bacon as a topping.")
            Total += 2
        elif selected_topping == "Extra cheese":
            print("You have selected Extra cheese as a topping.")
            Total += 3
        elif selected_topping == "None":
            print("You have selected no toppings.")
        else:
            print("Please enter a valid topping.")
    else:
        print("Please enter a valid topping.")
    add_more = input("Would you like to add more toppings? (yes/no): ")
    if add_more == "no":
        break        
        
# Display the order summary to the user
print("Order Summary:")
print("Number of pizzas: ", num_pizzas)
print("Size of the pizzas: ", selected_size)
print("Toppings: ", selected_topping)
print("Total: $", Total)

#   Ask the user if they would like to pay with cash or card
payment_method = input("Would you like to pay with cash or card? ")
if payment_method == "cash":
    print("Please pay the total amount of $", Total, " in cash.")
elif payment_method == "card":
    print("Please enter your card details to pay the total amount of $", Total)
else:
    print("Please enter a valid payment method.")

#   Thank the user for using the pizza ordering machine
print("Thank you for using the pizza ordering machine! Enjoy your pizza!")
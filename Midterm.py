# Romain Tranchant
# Fundamentals of programing
# Instructor: MD Ali
# Midterm assignment
# Programming Fundamentals and Problem Solving
# Date: 10/20/2024

# Assignment Overview:
# You are required to create a Python program that will help a small business manage their
# customer orders. The program should handle the following tasks:
# 1. Customer Information Management (10 points)
# - Allow the user to input a customer’s name and contact information (name, phone number, and
# email).
# - Validate that the phone number and email are in the correct format.

# 2. Product Ordering System (10 points)
# - The system should allow customers to choose products from a predefined list of at least five
# items, each with a unique ID, name, and price.
# - The user should be able to input the product ID and the quantity for each item they wish to
# purchase.
# - Calculate the total cost of the order before tax (8.25% tax rate applied).

# 3. Discounts and Final Calculation (10 points)
# - If the total order is more than $100, apply a 10% discount before calculating the tax.
# - Display the final order amount after applying the tax and any applicable discount.

# 4. Program Structure (10 points)
# - The program should include at least the following functions:
# - A function to input and validate customer information.
# - A function to display the product list.
# - A function to calculate the total cost and apply discounts.
# - A main function to control the flow of the program.

# 5. Error Handling (5 points)
# - Ensure that your program handles invalid inputs (e.g., non-numeric input when a number is
# expected).
# - If the user enters an invalid product ID, prompt them to try again.

# 6. Extra Credit (Optional) (10 points)
# - Add functionality to store each order in a text file and include a summary of all customer
# orders at the end of the session.
# - Allow the user to choose between delivery and pickup, and charge a flat $10 delivery fee if
# delivery is chosen.

# Submission Requirements:
# - Submit your Python program as a `.py` file.
# - Your code should be well-commented, with a header comment block explaining the program,
# its author, and the date. Each function should also have a brief comment explaining its purpose.
# - Include sample input and output in a separate text file.

# Grading Rubric:
# Functionality (10 points): Program meets all requirements and handles inputs correctly.
# Modularity (10 points): Use of functions to separate logic appropriately.
# Code Quality (10 points): Code is well-organized, readable, and follows proper naming
# conventions.
# Error Handling (5 points): Program handles errors without crashing.
# Comments and Documentation (5 points): Clear, meaningful comments throughout the code

########################################################################################

# This program helps a small business to manage customer orders by collecting customer information,
# displaying available products, and processing orders. It uses regular expressions to validate phone
# numbers and email addresses, ensuring accurate input. Customers can enter product IDs and
# quantities, while the program calculates the total price, applies discounts for orders over $100, and
# adds sales tax at a rate of 8.25%. The user can choose between delivery (with a $10 fee) or pickup. Finally,
# the program summarizes the order details and saves them to a "receipt.txt" file. The main function
# controls the program flow, executing when the script runs directly.

########################################################################################


# Import the regular expression module to validate phone numbers and emails' format
import re

# define a valid_phone function to validate phone numbers
def valid_phone(phone):
# Compile a regular expression pattern to validate phone numbers in the formats (123) 456-7890
# or 123-456-7890
    pattern = re.compile(r'^(\(\d{3}\) |\d{3}-)\d{3}-\d{4}$')
# Match the input phone number against the compiled pattern and return the match object or None
    return pattern.match(phone)

# Define a function to validate email addresses
def valid_email(email):
# Compile a regular expression for validating standard email formats, a valid format includes
# upper and lower cases, number, and special characters. An example of a valid format is example@domain.com
    pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
# Match the input email against the compiled pattern and return the match object or None
    return pattern.match(email)

# Define a customer_info function to get and validate the customer's information
def customer_info():
# Ask the user for the customer's name
    name = input("Enter customer's name: ")
# Ask the user for the customer's phone number
    phone = input("Enter customer's phone number (format: 123-456-7890 or (123) 456-7890): ")

# Start a while loop to get user's input and check the validity of the phone number
    while not valid_phone(phone):
# Inform the user of invalid input and prompt again
        print("Invalid phone number format. Please try again.")
        phone = input("Enter customer's phone number: ")

# Ask the user for the customer's email
    email = input("Enter customer's email (format: example@domain.com): ")

# Start a while loop to get user's input and check the validity of the email address
    while not valid_email(email):
# Inform the user of invalid input and prompt again
        print("Invalid email format. Please try again.")
        email = input("Enter customer's email: ")

# Print the collected customer information after error checking
    print("Customer Information:")
    print(f"Name: {name}")
    print(f"Phone: {phone}")
    print(f"Email: {email}")

# Return the customer information as a dictionary
    return {"name": name, "phone": phone, "email": email}

# Predefined a product dictionary, the dictionary allows the items to be associated with ID number,
# Item name and price
products_dict = {
    1: {"Item": "Fork", "Price": 14},    # Product ID 1 with name and price
    2: {"Item": "Knife", "Price": 16},   # Product ID 2 with name and price
    3: {"Item": "Spoon", "Price": 15},   # Product ID 3 with name and price
    4: {"Item": "Cup", "Price": 10},     # Product ID 4 with name and price
    5: {"Item": "Plate", "Price": 12},   # Product ID 5 with name and price
}

# Define a display_products function to display the product list
def display_products():
# Print a header for available products and inform the customers about the discount
    print("Available Products:")
    print("10% Discount for orders above $100")
# Loop through each product in the product dictionary
    for product_id, details in products_dict.items():
# Print each product's ID, name, and price formatted to two decimal places
        print(f"ID: {product_id}, Item: {details['Item']}, Price: ${details['Price']:.2f}")

# Define a get_order function to get the order from the customer
def get_order():
# Create an empty dictionary to store the order
    order = {}
# Start a while loop to allow multiple inputs
    while True:
# Ask the customer to enter a product ID and store it in the product_id variable, or finish with 0
        product_id = input("Enter product ID to purchase (or press 0 to finish): ")
# Validate that the product ID is a digit and non-negative
        if not product_id.isdigit() or int(product_id) < 0:
# Print an invalid input message and skip to the next iteration if the input is invalid through
# the continue statement
            print("Invalid input. Please enter a valid product ID or press 0 to finish.")
            continue
# Convert the product ID to an integer
        product_id = int(product_id)
# Exit the loop if 0 is entered through the break statement
        if product_id == 0:
            break

# Check if the entered product ID exists in the products dictionary
        if product_id in products_dict:
# Ask the user to enter the quantity for the selected product
            quantity = input(f"Enter quantity for {products_dict[product_id]['Item']}: ")
# Validate that the quantity is a digit
            if not quantity.isdigit():
# Print an invalid input message and skip to the next iteration if the input is invalid through
# the continue statement
                print("Invalid quantity. Please enter a numeric value.")
                continue
# Convert the quantity to an integer and store the product ID and its quantity in the order dictionary
            quantity = int(quantity)
            order[product_id] = quantity
# Inform the user of an invalid product ID
        else:
            print("Invalid product ID. Please try again.")
# Return the completed order dictionary
    return order

# Define a calculate_total function to calculate total cost and apply discounts
def calculate_total(order):
# Calculate the total cost by summing the price of each product multiplied by its quantity
    total = sum(products_dict[pid]["Price"] * qty for pid, qty in order.items())
# Create a discount variable to zero
    discount = 0
# Check if the total exceeds $100 for discount eligibility
    if total > 100:
# Calculate a 10% discount and deduct the discount from the total and print the discount applied
        discount = total * 0.10
        total -= discount
        print(f"Discount applied: ${discount:.2f}")

# Define the sales tax rate (8.25%) and calculate total including tax
    tax_rate = 0.0825
    total_with_tax = total * (1 + tax_rate)
# Return both the total and the total with tax
    return total, total_with_tax

# Define the delivery_option function to determine delivery option and fee
def delivery_option():
# Start an infinite loop to ensure valid input
    while True:
# Ask the user to choose delivery or pickup and convert input to uppercase
        delivery_option = input("Choose between delivery $10 press (D) or pickup press (P):").upper()
# Check if the input is valid (either 'D' or 'P')
        if delivery_option in ['D', 'P']:
# Return a delivery fee of $10 for delivery or $0 for pickup
            return 10 if delivery_option == 'D' else 0
# Inform user of invalid choice
        else:
            print("Invalid choice. Please enter 'D' for delivery or 'P' for pickup.")

# Define a format_order function to format order for the output
def format_order(order):
# Create a formatted string representing the order, listing the product names and quantities
    return ", ".join(f"{products_dict[pid]['Item']}: {qty}" for pid, qty in order.items())

# Define a save_order function to save order to a text file
def save_order(customer_info_data, order, delivery_fee, total_price, total_with_tax):
# Open or create if necessary a file named "receipt.txt" in append mode to save the order information
    with open("receipt.txt", "a") as receipt:
# Write the customer's name
        receipt.write(f"Customer: {customer_info_data['name']}\n")
# Write the customer's phone number
        receipt.write(f"Phone: {customer_info_data['phone']}\n")
# Write the customer's email
        receipt.write(f"Email: {customer_info_data['email']}\n")
# Write the formatted order
        receipt.write(f"Order: {format_order(order)}\n")
# Write the delivery fee
        receipt.write(f"Delivery Fee: ${delivery_fee:}\n")
# Write total price after discounts
        receipt.write(f"Total Price (after discounts): ${total_price:.2f}\n")
# Write total price after tax
        receipt.write(f"Total Price (after tax, 8.25%): ${total_with_tax:.2f}\n")

# Define a main function and call the functions in the right order to control the flow of the program
def main():

# Get the customer information and sore it in the customer_info_data variable
    customer_info_data = customer_info()
# Display the list of available products
    display_products()
# Get the customer's order and store it in the order variable
    order = get_order()
# Calculate the total price and total with tax
    total_price, total_with_tax = calculate_total(order)
# Determine the delivery option and fee and store it in the delivery_fee variable
    delivery_fee = delivery_option()
# Add the delivery fee to the total with tax
    total_with_tax += delivery_fee
# Print the summary of the order
    print("Order Summary:")
    print(f"Customer Name: {customer_info_data['name']}")
    print(f"Customer Phone Number: {customer_info_data['phone']}")
    print(f"Customer Email Address: {customer_info_data['email']}")
    print(f"Order: {format_order(order)}")
    print(f"Delivery Fee: ${delivery_fee:}")
    print(f"Total Price (after discounts): ${total_price:.2f}")
    print(f"Total Price (after tax, 8.25%): ${total_with_tax:.2f}")
# Save the customer's information and order details to a receipt.txt file
    save_order(customer_info_data, order, delivery_fee, total_price, total_with_tax)

# This block checks if the script is being run directly. If so, it calls the main() function
# to start the program. This allows the code to be reused as a module without executing
# the main logic when imported elsewhere.
if __name__ == "__main__":
    main()
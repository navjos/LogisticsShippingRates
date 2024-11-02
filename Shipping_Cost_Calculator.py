# Shipping Cost Calculator

## Input package weight and shipping rate

# the input function in Python is used to take an input from a user
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))


## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
# An f-string in Python, or formatted string literal, is a way to embed expressions inside string literals for easy and readable string formatting. 
print(f"Shipping Cost: {shipping_cost} USD")

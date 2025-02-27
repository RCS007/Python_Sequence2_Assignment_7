# Problem 2: Tax and Tip

# The program that you create for this exercise will begin by reading the cost of a meal
# ordered at a restaurant from the user. Then your program will compute the tax and tip for
# the meal.
# Use your local tax rate or 12% rate when computing the amount of tax owing. Compute
# the tip as 18 percent of the meal amount (without the tax). The output from your program
# should include the tax amount, the tip amount, and the grand total for the meal including
# both the tax and the tip.
# Format the output so that all of the values are displayed using two decimal places.


# Input the cost of the meal
meal_cost = float(input("Enter the cost of the meal: Rs "))

# Define tax and tip rates
tax_rate = 0.12  # 12% tax
tip_rate = 0.18  # 18% tip

# Calculate tax and tip amounts
tax_amount = meal_cost * tax_rate
tip_amount = meal_cost * tip_rate

# Calculate the total cost
total_cost = meal_cost + tax_amount + tip_amount

# Display the results with two decimal places
print(f"Tax amount: Rs {tax_amount:.2f}")
print(f"Tip amount: Rs {tip_amount:.2f}")
print(f"Grand total: Rs {total_cost:.2f}")

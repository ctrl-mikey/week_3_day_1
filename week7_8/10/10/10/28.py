# input for what delivery type
order_type = input("Order type (standard/express): ").lower()
location = input("Location (local/international): ").lower()
# flow chart on standart or not, express or not
if order_type == "standard" and location == "local":
    print("5-7 days")
elif order_type == "standard":
    print("15-20 days")
elif order_type == "express" and location == "local":
    print("1-2 days")
elif order_type == "express":
    print("5-10 days")
else:
    print("Invalid input.")


# Call the function

########################################## Question 7: energy Usage Billing 
#Ask the user for their total energy usage in kWh
usage = float(input("Enter your total energy usage in kWh: "))

# Ask if they are a registered low-income household
low_income = input("Are you a registered low-income household? (Y/N): ")

# Determine the applicable rate
if usage < 200:
    if low_income == "Y":
        print("Discounted rate of $0.08/kWh applies.")
    else:
        print("Standard rate of $0.10/kWh applies.")
elif 200 <= usage <= 500:
    print("Medium usage rate of $0.12/kWh applies.")
else:
    if low_income == "Y":
        print("Discounted high usage rate of $0.15/kWh applies.")
    else:
        print("High usage rate of $0.20/kWh applies.")

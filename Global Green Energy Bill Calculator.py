print("Hello! Welcome to the Global Green Energy bill calculator!")
acc = input("Please enter your Account Number. \n\t")
print("Welcome back to your personalized bill calculator, " + acc + "!")
month = input("Please enter the month number (e.g., for January, enter 1. \n\t")
electricity_plan = input("Please enter your electricity plan (EFIR or EFLR). \n\t")
electricity_amount = float(input("Please enter your electricity usage in month " + month + " (in kWh). \n\t"))
gas_plan = input("Enter the natural gas plan you are subscribed to (GFIR or GFLR). \n\t")
gas_amount = float(input("Enter the amount of gas that was used (in GJ). \n\t"))
province = input("Please enter the abbreviation of your province of residence (two letters). \n\t")

provincial_tax = 0.00
electricity_fee: float = 120.62
gas_fee: float = 1.32
new_amount1 = 0.00
new_amount2 = 0.00

while province != "ON" or province != "NB" or province != "NL" or province != "NS" or province != "PE":
    if province == "AB" or province == "BC" or province == "MB" or province == "NT" or province == "NU" or \
            province == "QC" or province == "SK" or province == "YT":
        provincial_tax = 0.05
        break
    if province == "ON":
        provincial_tax = 0.13
        break
    province = input("Please enter a valid province abbreviation: \n\t")
    if province == "NB" or province == "NL" or province == "NS" or province == "PE":
        provincial_tax = 0.15
        break
    print("Please enter a valid province abbreviation.")

if electricity_plan == "EFIR":
    if electricity_amount < 1000:
        new_amount1 = electricity_amount * 0.0836
    if electricity_amount > 1000:
        new_amount1 = ((1000 * 0.0836) + (electricity_amount - 1000) * 0.0941)

if electricity_plan == "EFLR":
    new_amount1 = electricity_amount * 0.0911

if gas_plan == "GFIR":
    if gas_amount < 950:
        new_amount2 = gas_amount * 0.0456
    if gas_amount > 950:
        new_amount2 = ((950 * 0.0456) + (gas_amount - 950) * 0.0589)

if gas_plan == "GFLR":
    new_amount2 = gas_amount * 0.0393

monthly_total = float((new_amount1 + new_amount2 + electricity_fee + gas_fee) * provincial_tax)
final_total1 = float((new_amount1 + new_amount2 + electricity_fee + gas_fee) + monthly_total)
final_total2 = str(round(final_total1, 2))

print("Thank you for your input! Your total amount due now is: $" + final_total2 + ".")

input("Please press ENTER to exit. \n\t")

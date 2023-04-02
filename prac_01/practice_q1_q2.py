# Q1
print("Electricity bill estimator")
cost = int(input("Enter cents per kWh: "))
daily_use = float(input("Enter daily use in kWh: "))
billing_days_number = int(input("Enter number of billing days: "))
estimated_bill = cost * daily_use * billing_days_number / 100
print(f"Estimated bill: ${estimated_bill:.2f}")

# Q2
print("Electricity bill estimator 2.0")
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
tariff = int(input("Which tariff? 11 or 31: "))
daily_use = float(input("Enter daily use in kWh: "))
billing_days_number = int(input("Enter number of billing days: "))
if tariff == 11:
    estimated_bill = TARIFF_11 * daily_use * billing_days_number
elif tariff == 31:
    estimated_bill = TARIFF_31 * daily_use * billing_days_number
print(f"Estimated bill: ${estimated_bill:.2f}")

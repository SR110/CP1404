# Q1
print("Electricity bill estimator")
cost = int(input("Enter cents per kWh: "))
daily_use = float(input("Enter daily use in kWh: "))
billing_days_num = int(input("Enter number of billing days: "))
esmt_bill = cost * daily_use * billing_days_num / 100
print(f"Estimated bill: ${esmt_bill:.2f}")

# Q2
print("Electricity bill estimator 2.0")
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
tariff = int(input("Which tariff? 11 or 31: "))
daily_use = float(input("Enter daily use in kWh: "))
billing_days_num = int(input("Enter number of billing days: "))
if tariff == 11:
    esmt_bill = TARIFF_11 * daily_use * billing_days_num
elif tariff == 31:
    esmt_bill = TARIFF_31 * daily_use * billing_days_num
print(f"Estimated bill: ${esmt_bill:.2f}")

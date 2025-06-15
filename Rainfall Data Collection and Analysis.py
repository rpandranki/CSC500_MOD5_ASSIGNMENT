years = int(input("Enter the number of years: "))
total_rainfall = 0
total_months = 0

for year in range(1, years + 1):
    for month in range(1, 13):
        rainfall = float(input(f"Enter the rainfall (in inches) for year {year}, month {month}: "))
        total_rainfall += rainfall
        total_months += 1

average_rainfall = total_rainfall / total_months
print(f"Number of months: {total_months}")
print(f"Total inches of rainfall: {total_rainfall:.2f}")
print(f"Average rainfall per month: {average_rainfall:.2f}")

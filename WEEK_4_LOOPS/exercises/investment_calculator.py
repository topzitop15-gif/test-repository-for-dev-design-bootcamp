# Ask for initial investment amount
# Ask for annual interest rate (as percentage)
# Ask for number of years of investment
# Calculate value each year, with compound interest
# Display year by year growth
# Show total profit at the end of the year

print("")

investment_amt = float( input ("Enter initial investment amount:"))
interest_rate = float(input("Enter annual interest rate (%):"))
years = int(input("Enter number of years:"))

print("\n" + "="* 50)
print("INVESTMENT GROWTH PROJECTION")
print("="* 50)
print(f"Initiall Investment: ₦{investment_amt:,.2f}")
print(f"Interest Rate: {interest_rate}%")
print (f"Invetsment Period: {years} years")
print("")

current_amt = investment_amt

#using a while loop 
loop_year = 1

while loop_year<= years:
    loop_year = loop_year + 1

# use loop to calculate and display the year-by-year growth

for year in range (1, years + 1):
    print (year)
     #Calculate the interest earned for the current year
    interest_earned = current_amt * (interest_rate/100)

    # Calculate the new amount (updated investment value) using compound interest formula
    current_amt = current_amt * (1 + interest_rate/100)

    #Display year-by-year growth
    print(f"Year {year}: ₦{current_amt:,.2f} | Interest: ₦{interest_earned:,.2f}")


total_profit = current_amt - investment_amt

print("")
print("="* 50)
print(f"Final Amount : ₦{current_amt:,.2f}")
print(f"Total_profit : ₦{total_profit:,.2f}")
print(f"Return on Investment : {(total_profit/investment_amt)*100:,.2f}%")
print("="* 50)
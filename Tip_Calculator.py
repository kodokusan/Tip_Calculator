#!/usr/bin/env python3
print("Welcome to the Tip Calculator")
total = float(input("What is the total bill? \n$"))
people = int(input("How many people to split the bill? \n"))
percentage = float(input("What percentage of tip would you like to give? 10, 12, or 15? \n")) / 100
tip = total * percentage
bill_with_tip = total + tip
each_bill = bill_with_tip/people
print(f"Each person should pay ${each_bill}")


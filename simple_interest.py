"""
Simple interest = (P * R * T) / 100
P = Principal Amount
R = Rate of Interest
T =  Time of Duration
"""

Principal = float(input("Enter Principal Amount: "))
Rate = float(input("Enter Rate Amount: "))
Time = float(input("Enter Time Amount: "))
si = (Principal * Rate * Time) / 100
print("simple interest si", int(si))

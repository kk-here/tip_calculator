print("Welcome to tip calculator!")
n= float(input("What was today's total bill: "))
t= int(input("How much tip would you like to give? 10,12 or 15? :" ))
m= int(input("How many people to split the bill? :"))

pay= (float(t)+n)/float(m)

print(f"Each person have to pay: {round(pay,3)}")
print ("Welcome to our electricity bill calculator!")
print ("Please enter the following details:")
name = input("Enter your name: ")
bill_number = input("Enter your bill number: ")
print("Thank you,", name, "! Your bill number is", bill_number)  
unitsconsumed = float(input("Enter the number of units consumed: "))


#condition
if unitsconsumed <200:
    bill_amount = unitsconsumed * 25
elif unitsconsumed >= 200 and unitsconsumed < 300:
    bill_amount = 200 * 40 + 5000
else:
    bill_amount = 200 * 55 + 10000

print("Your electricity bill amount is: ", bill_amount)

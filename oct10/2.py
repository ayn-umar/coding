#date and time
import datetime
now = datetime.datetime.now()
print("Welcome!")
print("Current date and time is: ", now)

#input
city = input("Enter your city: ")
print("You live in", city)
#specific input
temp = int(input("Enter the temperature in Celsius: "))
#condition
if temp > 25:
    print("It's a hot day")
elif temp > 15:
        print("It's a warm day")
else:
        print("It's a cold day")

print("Thank you for using the application!")


#calender
import calendar
print(calendar.calendar(now.year))
number = int(input("Enter a number: "))

original_number = number

num_digits = len(str(number))

sum = 0

while number > 0:
    digit = number % 10
    sum = sum + digit ** num_digits
    number = number // 10
if sum == original_number:
    print(original_number, "is an Armstrong number")
else:
    print(original_number, "is not an Armstrong number")
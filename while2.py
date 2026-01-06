# Taking a number
num = 1234
reverse = 0

# Looping until number becomes zero
while num > 0:
    digit = num % 10          # Extracting last digit
    reverse = reverse * 10 + digit
    num = num // 10           # Removing last digit

# Printing reversed number
print("Reversed number:", reverse)

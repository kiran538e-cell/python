#Password strength checker high, moderate, weak.
# Take password input from the user
password = input("Enter a password to check its strength: ")

# Check lengths for the rules
length = len(password)

# Flags to track character types
has_upper = False
has_lower = False
has_digit = False

# Loop through each character to check its type using string functions
for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True

# Determine password strength
if length >= 8 and has_upper and has_lower and has_digit:
    print("Password Strength: Strong")
elif length >= 6:
    print("Password Strength: Moderate")
else:
    print("Password Strength: Weak")
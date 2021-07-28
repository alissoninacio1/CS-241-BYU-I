"""
check09a.py exceptions
"""


made = False

while not made:
    try:
        number = int(input("Enter a number: "))
        made = True
    except ValueError:
        print("The value entered is not valid")

print(f"The result is: {number * 2}")

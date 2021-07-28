"""
check09b.py - more exceptions
"""

class NegativeNumberError(Exception):
  pass



def get_inverse(n):
    n_float = float(n)

    if n_float < 0:
        raise NegativeNumberError("Error: The value cannot be negative")

    return 1 / n_float


def main():
    n = input("Enter a number: ")
    try:
        result = get_inverse(n)
        print(f"The result is: {result}")
    except ValueError:
        print("Error: The value must be a number")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")


if __name__ == "__main__":
    main()

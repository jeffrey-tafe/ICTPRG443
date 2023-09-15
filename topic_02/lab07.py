fractions_file = open("fractions.txt", "rt")
fractions = fractions_file.readlines()
def divide(number, divisor):
  try:
    number = int(number)
    divisor = int(divisor)
    result = number / divisor
    print(f"{number} / {divisor} = {result}")
  except ZeroDivisionError as exception:
    print(type(exception).__name__)
  except ValueError as exception:
    print(type(exception).__name__)
  except Exception as exception:
    print(f"Unhandled Exception: {type(exception).__name__}")
    print(f"{exception}")



for fraction in fractions:
  number, divisor = fraction.split("/")
  divide(number, divisor)



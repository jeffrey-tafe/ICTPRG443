def divide_numbers(num1, num2):
  if num1.isalpha():
    raise ValueError("num1 must be a number")
  elif num2.isalpha():
    raise ValueError("num2 must be a number")

  num1 = int(num1)
  num2 = int(num2)

  if num2 == 0:
    raise ZeroDivisionError("Division by zero!")
  else:
    return num1/num2

def main():
  try:
    result = divide_numbers("2", "0")
  except Exception as e:
    print(f"Error - {e}")
    result = 0
  finally:
    print(f"Result = {result}")


main()

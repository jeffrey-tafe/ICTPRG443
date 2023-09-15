try:
  num1, num2 = eval(input("Enter two numbers, separated by a comma: "))
  result = num1 / num2
  print(f"Result is {result}")

except ZeroDivisionError:
  print("Division by zero is not possible")

except NameError:
  print("This needs to be a number")

except TypeError:
  print("A comma needs to serarate each number")

except SyntaxError:
  print("This needs to be entered as 'number,number")

except ValueError:
  print("Only 2 numbers required")

except Exception as e:
  print(f"An unhandled exception was encountered")
  print(f"Exception: {e}")
  print(f"Type of exception: {(type(e).__name__, e.args)}")

else:
  print("No errors")
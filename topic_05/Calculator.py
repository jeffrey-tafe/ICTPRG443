def add(n1,n2):
  return n1 + n2


def subtract(n1, n2):
  return n1 - n2


def multiply(n1, n2):
  return (n1 * n2)


def divide(num, den):
  if not num.isdigit() or not den.isdigit():
    raise ValueError("Number format Errors")
  den = int(den)
  if den == 0:
    raise ZeroDivisionError("Division By Zero Error")
  else:
    num = int(num)
  return num / den


def main():
  try:
    result = divide("A",5)
    print(f"The result is: ", result)
  except Exception as e:
    print(e)



if __name__ == "__main__":
  main()

try:
  product_file = open("product3s.txt", "rt")
  print("*" * 10)
  print("Products")
  print("*"*10)
  for line in product_file:
    print(line, end='')
  product_file.close()
except FileNotFoundError:
  print("Cannot open this file")
  print("Terminating program")
except Exception:
  print("An unhandled exception encountered")
  print("Terminating program")
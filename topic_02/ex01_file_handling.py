product_file = open("products.txt", "rt")

# Read whole file
# print(product_file.read())

# Read first 4 chars
# print(product_file.read(4))

# Read first line
# print(product_file.readline())

# Read lines, formatted for importing to a list
#print(product_file.readlines())

# Read line by line, with loop
# for line in product_file:
#         print(line)

# Read line by line, with loop and no extra line break
# for line in product_file:
#         print(line, end='')

# Read line by line, with loop and no extra line break alternative
# for line in product_file:
#         print(line, strip)

# Read line by line, with loop and no extra line break alternative
# for line in product_file:
#         print(line, rstrip)

# Read line by line, with loop and no extra line break alternative
# for line in product_file:
#         print(line, lstrip)

# Always close a file after opening/reading
product_file.close()
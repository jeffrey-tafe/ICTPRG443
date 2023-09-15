import os

# Prompt for file name
file_name = input("Enter a filename: ")

# Test file exists
file_exists = os.path.isfile(f"./{file_name}")
if not file_exists:
  print(f"{os.getcwd()}\\{file_name} not found ")
  quit()

# Read file contents
file_open = open(file_name, "rt")
content = file_open.read()
file_open.close()

# Count chars
count_char = len(content)
print(f"{count_char} characters")

# Count words
count_words = len(content.split())
print(f"{count_words} words")

# Count lines
file_open = open(file_name, "rt")
count_lines = len(file_open.readlines())
print(f"{count_lines} lines")

# Close file
file_open.close()
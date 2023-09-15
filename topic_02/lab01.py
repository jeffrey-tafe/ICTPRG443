import os

# Prompt for file name
file_name = input("Enter a filename: ")

# Test file exists
file_exists = os.path.isfile(f"./{file_name}")
if not file_exists:
  print(f"{os.getcwd()}\{file_name} not found ")
  quit()

# Prompt for string to remove
string_to_replace = input("Enter a string to replace: ").strip()

# Verify a valid string was entered
if string_to_replace == "":
  print("You must enter a string to replace")
  quit()

# Open file in write mode
file_read = open(file_name, "rt")
content = file_read.read()
print(f"\nFile before change\n{content}\n")
file_read.close()

# Replace instances of string
content = content.replace("test", "")

# Write string back to file
file_write = open(file_name, "wt")
file_write.write(content)

# Close file
file_write.close()

# Output result
file_read = open(file_name, "rt")
content = file_read.read()
file_read.close()
print(f"\nResult\n{content}")

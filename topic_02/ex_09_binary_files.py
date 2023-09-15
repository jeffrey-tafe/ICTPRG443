# # Write to binary file
# my_bin_file = open("binfile.bin", "wb")
# num = [5,10,15,20, 25]
# my_list = bytearray(num)
# my_bin_file.write(my_list)
# my_bin_file.close()

# Read from binary file
my_bin_file = open("binfile.bin", "rb")
binary_content = my_bin_file.read()
print(binary_content[0])

for item in binary_content:
  print(item)

  my_bin_file.close()
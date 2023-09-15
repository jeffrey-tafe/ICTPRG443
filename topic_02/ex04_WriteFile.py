my_file = open("demofile.txt", "at+")

my_file.write("Now the file has more content\n")

my_file.seek(0)

print(my_file.readline())

my_file.write("Next Line\n")

my_file.close()
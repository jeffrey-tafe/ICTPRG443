# import os
#
# try:
#   my_file = open("demofile2.txt", "a")
#   os.remove("demofile2.txt")
#   my_file.write("Now the file has more content!\n")
#
# except IOError as err:
#   print(f"File error - {err}")
# finally:
#   my_file.close()


import os

try:
  with open("demofile2.txt", "w") as my_file:
    os.remove("demofile2.txt")
    my_file.write("Now the file has more content!\n")
except IOError as err:
  print(f"File error - {err}")
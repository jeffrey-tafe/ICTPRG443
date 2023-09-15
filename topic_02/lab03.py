import os
from statistics import mean

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

# Get number of scores
score_count = len(content.split())
print(f"There are {score_count} scores")

# Get total scores
scores = content.split()
scores = list(map(int, scores))
score_total = sum(scores)
print(f"The total is {score_total}")

# Get average score
score_average = mean(scores)
print(f"The average is {score_average}")
# Which of the following dictionaries are created correctly?
# d = {1: [1, 2], 3: [3, 4]}
# d = {[1, 2]: 1, [3, 4]: 3}
# d = {(1, 2): 1, (3, 4): 3}
# d = {1: "John", 3: "peter"}
# d = {"john": 1, "peter": 3}
# Al but the second manages to compile correctly

#Suppose a dictionary named students is {"john": 3, "peter":2}. What do the following statements do?
# (a) students["susan"] = 5     - Adds susan student to dictionary
# (b) students["peter"] = 5     - Overwrites peter student
# (c) students["peter"] += 5    - Updates the value of peter student to current plus 5
# (d) del students["peter"]     - Deletes the peter student from dictionary

#Show the output of the following code:
# def main():
#     d = {"red": 4, "blue": 1, "green" : 14, "yellow":2}
#     print(d["red"])
#     print(list(d.keys()))
#     print(list(d.values()))
#     print("blue" in d)
#     print("purple" in d)
#     d["blue"] += 10
#     print(d["blue"])
#
# main()
#
# Output
#
# 4
# ['red', 'blue', 'green', 'yellow']
# [4, 1, 14, 2]
# True
# False
# 11

# For a dictionary d, you can use d[key] or d.get(key) to return the value for the key.
# What are the differences between them?
# The difference is how you want to handle missing keys.
# d[key] will return a KeyError if not found
# d.get(key) will return a default value, usually None, if the key is not found.
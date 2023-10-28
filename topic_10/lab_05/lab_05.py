# What is wrong with the following code?
# t = (1, 2, 3)
# t.append(4)
# t.remove(0)
# t[0] = 1
# Cannot make changes to a tuple

# Is the following code correct
# t1 = (1, 2, 3, 7, 9, 0, 5)
# t2 = (1, 2, 5)
# t1 = t2
#  t1 will be overwritten with the content of t2

# Show the print out of the following code
# t = (1, 2, 3, 7, 9, 0, 5)
# print(t)
# print(t[0])
# print(t[1:3])
# print(t[-1])
# print(t[:-1])
# print(t[1:-1])

# Shot the printout of the following code
# t = (1, 2, 3, 7, 9, 0, 5)
# print(max(t))
# print(min(t))
# print(sum(t))
# print(len(t))

# Show the printout of the following code
t1 = (1, 2, 3, 7, 9, 0, 5)
t2 = (1, 3, 22, 7, 9, 0, 5)
print(t1 == t2)
print(t1 != t2)
print(t1 > t2)
print(t1 < t2)

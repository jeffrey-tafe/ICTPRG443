# Write a program that counts the occurrences of words in a text file (use your own) and displays
# the ten most frequently used words in decreasing order of their occurrence counts.
#
# HINT: Use a Dictionary to store each word and its count. Ignore case and treat them as the
# same word (example Good is treated the same as good)


# Get text from file
with open("ipsum.txt") as file:
    text = file.read()
    text = text.lower()

# Get unique words in string as set then convert to list
text_list = text.split()
words = list(set(text.split()))

# Iterate through words list
# search for instance of word in text string
# save count in dictionary with word as key

word_counts = {}

for word in words:
    count = text_list.count(word)
    word_counts[word] = count

word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
word_counts_list = list(word_counts)

for word in word_counts_list[:10]:
    print(word)

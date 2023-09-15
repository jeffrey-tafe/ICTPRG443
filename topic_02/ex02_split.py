# Split string
string1 = "Person1: Hello, how are you?"
string2 = "Person2: I'm very well: thank you."

actor, line_spoken = string1.split(":")
print(f"Actor: {actor}")
print(f"Line: {line_spoken}")

actor, line_spoken = string2.split(":", 1)
print(f"Actor: {actor}")
print(f"Line: {line_spoken}")
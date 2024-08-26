# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4

string = "hello world"

char = input("Which chaacter would you like to match?")

index = string.index(char)

print(index)


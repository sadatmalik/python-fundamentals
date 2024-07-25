# Proof that the following file is a .pdf file using a `for` loop.
# - Don't use the string method you've used to solve this before!
# - Don't use the `in` keyword to look for a sub-string!
# - Don't use any string slicing technique either!
#
# You'll see that it'll be tricky to solve this challenge with a loop :)
# Remember to use also other techniques you've learned,
# for example flags and conditional statements.

filename = "operators.pdf"
pdf = ".pdf"

match = False
i = 0
for char in filename:
    if i < 4 and char == pdf[i]:
        match = True
        i += 1
    else:
        match = False
        i = 0

print(match)


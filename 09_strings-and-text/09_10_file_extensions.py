# Use a Python string method to prove which of the following files
# are .pdf files, and which aren't.
# Call the method on each file string and print() Python's response.

file_1 = "operators.pdf"
file_2 = "snowfall.jpg"
file_3 = "uncle-joes-wedding.doc"
file_4 = "invitation.pdf"

def is_pdf(file):
    return file.endswith(".pdf")

print(is_pdf(file_1))
print(is_pdf(file_2))
print(is_pdf(file_3))
print(is_pdf(file_4))

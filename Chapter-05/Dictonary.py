# marks = {
#     "Faizan" : 78,
#     "Tahir" : 56,
#     "Sohail" : 67,
#     "Ali" : 93,
# }

# print(marks, type(marks))
# print(marks["key"]) # Output: "value"
# print(marks["list"]) # Output: [1, 2, 9]

# print(marks["Faizan"])


            # Method Of Dictionary

marks = {
    "Faizan" : 78,
    "Tahir" : 56,
    "Sohail" : 67,
    "Ali" : 93,
}

# print(marks.items()) # For all items

# print(marks.keys()) # For All Keys

# print(marks.values()) # For All Value

# marks.update({"Faizan" : 85}) # For Update Values
# print(marks)

print(marks.get("Sohail")) # For Find the key and give value
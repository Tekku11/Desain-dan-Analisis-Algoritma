# Slide 34
# Get matching substrings in string
# Initializing string
test_str = "GfG is good website"

# Initializing potential substrings
test_list = ["GfG", "site", "CS", "Geeks", "Tutorial"]

# Printing original string
print("The original string is : " + test_str)

# Printing potential strings list
print("The original list is : " + str(test_list))

# Using list comprehension
# Get matching substrings in string
res = [sub for sub in test_list if sub in test_str]

# Printing result
print("The list of found substrings : " + str(res))
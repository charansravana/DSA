# A single script to demonstrate all major Python string methods for quick revision.

# capitalize(): Converts the first character to upper case.
print("## capitalize() ##")
txt_capitalize = "hello, and welcome to my world."
print("Original:", txt_capitalize)
print("Capitalized:", txt_capitalize.capitalize())
print("-" * 20)

# casefold(): Converts string into a more aggressive lower case for caseless matching.
print("## casefold() ##")
txt_casefold = "Straße"  # German sharp s
print("Original:", txt_casefold)
print("Casefolded:", txt_casefold.casefold()) # Compares equal to 'strasse'
print("-" * 20)

# center(): Returns a centered string.
print("## center() ##")
txt_center = "banana"
print("Centered:", txt_center.center(20, "-"))
print("-" * 20)

# count(): Returns the number of times a specified value occurs in a string.
print("## count() ##")
txt_count = "I love apples, apple are my favorite fruit."
print(f"'{txt_count}'.count('apple') is:", txt_count.count("apple"))
print("-" * 20)

# encode(): Returns an encoded version of the string.
print("## encode() ##")
txt_encode = "My name is Ståle"
print("Encoded (utf-8):", txt_encode.encode())
print("-" * 20)

# endswith(): Returns true if the string ends with the specified value.
print("## endswith() ##")
txt_endswith = "Hello, welcome to my world."
print(f"'{txt_endswith}'.endswith('.') is:", txt_endswith.endswith("."))
print("-" * 20)

# expandtabs(): Sets the tab size of the string.
print("## expandtabs() ##")
txt_expandtabs = "H\te\tl\tl\to"
print("Original:", txt_expandtabs)
print("Tab size 4:", txt_expandtabs.expandtabs(4))
print("-" * 20)

# find(): Searches the string for a value and returns the position, or -1 if not found.
print("## find() ##")
txt_find = "Hello, welcome to my world."
print("Position of 'welcome':", txt_find.find("welcome"))
print("Position of 'galaxy':", txt_find.find("galaxy"))
print("-" * 20)

# format(): Formats specified values in a string.
print("## format() ##")
txt_format = "For only {price:.2f} dollars!"
print(txt_format.format(price=49.99))
print("-" * 20)

# format_map(): Formats specified values in a string using a dictionary.
print("## format_map() ##")
point = {'x': 4, 'y': -5}
print("Point coordinates: {x}, {y}".format_map(point))
print("-" * 20)

# index(): Searches the string for a value and returns the position, but raises an error if not found.
print("## index() ##")
txt_index = "Hello, welcome to my world."
print("Position of 'welcome':", txt_index.index("welcome"))
# print(txt_index.index("galaxy")) # This line would cause a ValueError
print("-" * 20)

# isalnum(): Returns True if all characters are alphanumeric.
print("## isalnum() ##")
txt_isalnum1 = "Company123"
txt_isalnum2 = "Company 123"
print(f"'{txt_isalnum1}'.isalnum() is:", txt_isalnum1.isalnum())
print(f"'{txt_isalnum2}'.isalnum() is:", txt_isalnum2.isalnum())
print("-" * 20)

# isalpha(): Returns True if all characters are in the alphabet.
print("## isalpha() ##")
txt_isalpha = "CompanyName"
print(f"'{txt_isalpha}'.isalpha() is:", txt_isalpha.isalpha())
print("-" * 20)

# isascii(): Returns True if all characters are ascii characters.
print("## isascii() ##")
txt_isascii = "Hello123"
print(f"'{txt_isascii}'.isascii() is:", txt_isascii.isascii())
print("-" * 20)

# isdecimal(): Returns True if all characters are decimals (0-9).
print("## isdecimal() ##")
txt_isdecimal = "12345"
print(f"'{txt_isdecimal}'.isdecimal() is:", txt_isdecimal.isdecimal())
print("-" * 20)

# isdigit(): Returns True if all characters are digits.
print("## isdigit() ##")
txt_isdigit = "50800"
print(f"'{txt_isdigit}'.isdigit() is:", txt_isdigit.isdigit())
print("-" * 20)

# isidentifier(): Returns True if the string is a valid identifier.
print("## isidentifier() ##")
txt_isidentifier1 = "MyVariable"
txt_isidentifier2 = "2MyVariable"
print(f"'{txt_isidentifier1}'.isidentifier() is:", txt_isidentifier1.isidentifier())
print(f"'{txt_isidentifier2}'.isidentifier() is:", txt_isidentifier2.isidentifier())
print("-" * 20)

# islower(): Returns True if all characters are lower case.
print("## islower() ##")
txt_islower = "hello world!"
print(f"'{txt_islower}'.islower() is:", txt_islower.islower())
print("-" * 20)

# isnumeric(): Returns True if all characters are numeric.
print("## isnumeric() ##")
txt_isnumeric = "565543"
print(f"'{txt_isnumeric}'.isnumeric() is:", txt_isnumeric.isnumeric())
print("-" * 20)

# isprintable(): Returns True if all characters are printable.
print("## isprintable() ##")
txt_isprintable = "Hello! Are you #1?"
txt_isprintable2 = "Hello!\nAre you #1?" # \n is not printable
print(f"'{txt_isprintable}'.isprintable() is:", txt_isprintable.isprintable())
print(f"'{txt_isprintable2}'.isprintable() is:", txt_isprintable2.isprintable())
print("-" * 20)

# isspace(): Returns True if all characters are whitespaces.
print("## isspace() ##")
txt_isspace = "   "
print(f"'{txt_isspace}'.isspace() is:", txt_isspace.isspace())
print("-" * 20)

# istitle(): Returns True if the string follows the rules of a title.
print("## istitle() ##")
txt_istitle = "Hello, And Welcome To My World!"
print(f"'{txt_istitle}'.istitle() is:", txt_istitle.istitle())
print("-" * 20)

# isupper(): Returns True if all characters are upper case.
print("## isupper() ##")
txt_isupper = "HELLO WORLD!"
print(f"'{txt_isupper}'.isupper() is:", txt_isupper.isupper())
print("-" * 20)

# join(): Joins the elements of an iterable to the end of the string.
print("## join() ##")
my_tuple = ("John", "Peter", "Vicky")
print("Joined with '#':", "#".join(my_tuple))
print("-" * 20)

# ljust(): Returns a left justified version of the string.
print("## ljust() ##")
txt_ljust = "banana"
print(txt_ljust.ljust(20), "is my favorite fruit.")
print("-" * 20)

# lower(): Converts a string into lower case.
print("## lower() ##")
txt_lower = "Hello my FRIENDS"
print("Lowercased:", txt_lower.lower())
print("-" * 20)

# lstrip(): Returns a left trim version of the string.
print("## lstrip() ##")
txt_lstrip = "     banana     "
print("Left stripped:", txt_lstrip.lstrip(), "is a fruit.")
print("-" * 20)

# maketrans() and translate(): Create and use a translation table.
print("## maketrans() & translate() ##")
txt_trans = "Hello Sam!"
mytable = str.maketrans("S", "P")
print("Translated:", txt_trans.translate(mytable))
print("-" * 20)

# partition(): Returns a tuple where the string is parted into three parts.
print("## partition() ##")
txt_partition = "I could eat bananas all day"
print("Partitioned on 'bananas':", txt_partition.partition("bananas"))
print("-" * 20)

# replace(): Returns a string where a specified value is replaced with a specified value.
print("## replace() ##")
txt_replace = "I like bananas"
print("Replaced:", txt_replace.replace("bananas", "apples"))
print("-" * 20)

# rfind(): Searches the string for a value and returns the last position, or -1.
print("## rfind() ##")
txt_rfind = "Mi casa, su casa."
print("Last position of 'casa':", txt_rfind.rfind("casa"))
print("-" * 20)

# rindex(): Searches the string for a value and returns the last position, but raises an error.
print("## rindex() ##")
txt_rindex = "Mi casa, su casa."
print("Last position of 'casa':", txt_rindex.rindex("casa"))
# print(txt_rindex.rindex("amigo")) # This would cause a ValueError
print("-" * 20)

# rjust(): Returns a right justified version of the string.
print("## rjust() ##")
txt_rjust = "banana"
print(txt_rjust.rjust(20), "is my favorite fruit.")
print("-" * 20)

# rpartition(): Returns a tuple where the string is parted into three parts from the right.
print("## rpartition() ##")
txt_rpartition = "I could eat bananas all day, bananas are my favorite"
print("Right partitioned on 'bananas':", txt_rpartition.rpartition("bananas"))
print("-" * 20)

# rsplit(): Splits the string at the separator, and returns a list (from the right).
print("## rsplit() ##")
txt_rsplit = "apple, banana, cherry"
print("Right split once:", txt_rsplit.rsplit(", ", 1))
print("-" * 20)

# rstrip(): Returns a right trim version of the string.
print("## rstrip() ##")
txt_rstrip = "     banana     "
print("Right stripped:", txt_rstrip.rstrip(), "is a fruit.")
print("-" * 20)

# split(): Splits the string at the separator, and returns a list.
print("## split() ##")
txt_split = "welcome to the jungle"
print("Split by space:", txt_split.split())
print("-" * 20)

# splitlines(): Splits the string at line breaks and returns a list.
print("## splitlines() ##")
txt_splitlines = "Thank you for the music\nWelcome to the jungle"
print("Split into lines:", txt_splitlines.splitlines())
print("-" * 20)

# startswith(): Returns true if the string starts with the specified value.
print("## startswith() ##")
txt_startswith = "Hello, welcome to my world."
print(f"'{txt_startswith}'.startswith('Hello') is:", txt_startswith.startswith("Hello"))
print("-" * 20)

# strip(): Returns a trimmed version of the string.
print("## strip() ##")
txt_strip = "     banana     "
print("Stripped:", txt_strip.strip(), "is a fruit.")
print("-" * 20)

# swapcase(): Swaps cases, lower case becomes upper case and vice versa.
print("## swapcase() ##")
txt_swapcase = "Hello My Name Is PETER"
print("Swapped case:", txt_swapcase.swapcase())
print("-" * 20)

# title(): Converts the first character of each word to upper case.
print("## title() ##")
txt_title = "Welcome to my world"
print("Title cased:", txt_title.title())
print("-" * 20)

# upper(): Converts a string into upper case.
print("## upper() ##")
txt_upper = "Hello my friends"
print("Uppercased:", txt_upper.upper())
print("-" * 20)

# zfill(): Fills the string with a specified number of 0 values at the beginning.
print("## zfill() ##")
txt_zfill = "50"
print("Zero-filled to length 5:", txt_zfill.zfill(5))
print("-" * 20)
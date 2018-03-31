# Create a function named stringcases that takes a single string but returns a tuple of different string formats. The formats should be:

# * All uppercase
# * All lowercase
# * Titlecased(first letter of each word is capitalized)
# * Reversed
# There are str methods for all but the last one.


def stringcases(my_string):
      return (my_string.upper(), my_string.lower(), my_string.title(), my_string[::-1])

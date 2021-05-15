
# Lexing
# A way of extracting needed information from text.

# For example:
text = "Hello, World!";

# Imagine that we only need the words
# without any punctuation.
expected = ["Hello", "World"];

# So lexing (in out example)
# is basically converting from `text` to `expected`.


import re
def remove_punct(s):
	return re.sub(r"[^a-zA-Z]", '', s)

words = text.split()
final = list(map(remove_punct, words))

print(final if final == expected else "Error! " + str(final))

# But why do we need this?
# Because all the later stages don't
# care about all the comments, whitespace
# and unnecesary things! With each stage
# we abstract out the things that we don't need! 

# An actual lexer for a programming language
# Converts text into *tokens*.
# A token is a simple structure that contains
# it's type and it's value.
class Token:
	def __init__(self, type, value):
		self.type = type
		self.value = value

	def __str__(self):
		return f"Token({self.type}, {self.value})"

# For simple mathematical expressions, such as
# 1 + 2, 5 * (6 - 3), 4 / 3 + 2
# we only have a handful of token types:
TOKEN_TYPES = [
	"number",
	"add",
	"substract",
	"multiply",
	"divide",
	"opening paren",
	"closing paren",
]

import re

# Lexing
# A way of extracting needed information from text.
if __name__ == '__main__':
	# For example:
	text = "Hello, World!";

	# Imagine that we only need the words
	# without any punctuation.
	expected = ["Hello", "World"];

	# So lexing (in out example)
	# is basically converting from `text` to `expected`.

	from typing import ByteString
	def remove_punct(s):
		return re.sub(r"[^a-zA-Z]", '', s)

	words = text.split()
	final = list(map(remove_punct, words))

	print("Lexing '" + text + "'")
	print("Expeceted:", expected)
	print("Got: ", final)

# But why do we need this?
# Because all the later stages don't
# care about all the comments, whitespace
# and unnecesary things! With each stage
# we abstract out the things that we don't need! 


# An actual lexer for a programming language
# Converts text into *tokens*.
# A token is a simple structure that contains
# it's type and it's value.
# For simple mathematical expressions, such as
# 1 + 2, 5 * (6 - 3), 4 / 3 + 2
# we only have a handful of token types:
TOKEN_TYPES = [
	"number",
	"add",
	"substract",
	"multiply",
	"divide",
	"opening", # parenthesis
	"closing", # parenthesis
]

class Token:
	def __init__(self, type, value):
		if type not in TOKEN_TYPES:
			raise KeyError("Wrong token type!")
		self.type = type
		self.value = value

	def __repr__(self):
		if self.value:
			return f"Token({self.type}, {self.value})"
		else:
			return f"Token({self.type})"


def lex(input_string):
	tokens = [] # The resulting token list.
	index = 0
	last = len(input_string)
	while index < last:
		c = input_string[index]
		if c == ' ':
			# Have a space!! We don't need any spaces!
			index += 1 # Go to the next character.
			continue # Skip the space!

		if re.match(r"[0-9]", c):
			# How nice! or character is a digit!
			n = "" # The value of the token.

			# While we have a digit:
			while re.match(r"[0-9]", c):
				# Add the chatacter to the resulting value.
				n += c 
				
				# Next character
				if index + 1 < last:
					index += 1
					# Check if we have reached the end.
					c = input_string[index]
				else:
					break
			else:
				# This gets run if we did not
				# break out of the loop above
				# Since we incremented the index
				# and the current character is not
				# a didigt, we need to go back.
				index -= 1

			# Add the new token to the list.
			tokens.append(Token("number", n))


		elif c == '+':
			# We don't need a value here since
			# we already know that it's a `plus`
			# Such tokens are called *atoms*
			tokens.append(Token("add", ""))
		elif c == '-': tokens.append(Token("substract", ""))
		elif c == '*': tokens.append(Token("multiply", ""))
		elif c == '/': tokens.append(Token("divide", ""))
		elif c == '(': tokens.append(Token("opening", ""))
		elif c == ')': tokens.append(Token("closing", ""))
		else:
			# Oh well, we don't know what the character is!
			raise Exception(f"Unknown character {c}")

		# Remember to increace the index.
		index += 1

	return tokens

if __name__ == '__main__':

	# Let's see if this works:
	def check_lexer(expr):
		tokens = lex(expr)
		print("\n-------- TEST START --------\n")
		print("Expression: '" + expr + "'")
		print("Result:", tokens)
		print("\n-------- TEST END --------\n")

	print("\n========= LEXING TESTS =========\n")
	list(map(check_lexer, [
		"1 + 2",
		"1 - 2",
		"1 + 2 * 3 * (3 + 4)",
	]))	

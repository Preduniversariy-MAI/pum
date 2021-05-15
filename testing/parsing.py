# Parsing.
# One of the most hard to understand
# parts of a programming language!

# Take for example a simple
# mathematical expression:

from testing.lexing import Token, lex
from typing import Any


expression = "1 + 2"

# We need to somehow evaluate it.
# You might say:
# Well, we could just add the 1 and 2!
# Ok, what if we now have this:

1 - 3

# You say:
# Well, we look at the operator in between
# and do whatever the operation we need!
# How about this?

1 - 3 * 4

# What do you do now? And this:

6 * 3 - 4 / 5 + (8 * 9)

# *This* is why we need parsing!
# But what does parsing text do?
# It converts our expressions,
# statements, function calls into
# a *tree*, called an AST, or an
# Abstract Syntax Tree.
# How does it look?
# For 1 + 2, like this:
#*     (+)
#*    /  \
#*   1    2
# And for 2 + (3 - 4):
#*     (+)
#*    /  \____
#*   2        \
#*           (-)
#*           / \
#*          3   4
# So the operations are the parent
# nodes!
# What about 1 + 2 + 3? Like this:
#*     (+)
#*    /  \___
#*   1       \
#*          (+)
#*         /  \
#*        2    3
# Note: this could be the other way:
# 1 on the right and the second (+) on the left.
# Note: (+) could acutally have more
# child nodes, but it is harder to
# implement (we might do that actually)
# What do we do with parentheses? 1 + (2 + 3)?
# The AST doesn't change!
#*     (+)
#*    /  \___
#*   1       \
#*          (+)
#*         /  \
#*        2    3
# Note: But this time the tree can look
# only like this (if don't optimize stuff)

# Now! how do we convert 1 + 2 into a tree?
# There are many ways of doing this, but
# I will be going over top-down parsing.

# An empty base class for nodes of a tree
class Node:
	def __init__(self):
		self.node_type = self.__class__.__name__
	def print(self, i=0): pass

# This node represents a number
class NumberNode(Node):
	def __init__(self, value: int):
		self.value = value
	
	def print(self, i=0):
		print(i * ' ', 'Number -> ', self.value, sep='')

# This node represents an operation such as +, -, *, /
class OperationNode(Node):
	def __init__(self, type: str, left: Node, right: Node):
		self.type = type
		self.left = left
		self.right = right

	def print(self, i=0):
		print(i * ' ', '(' + self.type + ') ->', sep='')
		self.left.print(i + 4)
		self.right.print(i + 4)


class Parser:
	def __init__(self, tokens: list[Token]):
		self.tokens = tokens
		self.last = len(self.tokens)
		self.index = -1

	def next(self):
		# Return the next token
		self.index += 1
		if self.index >= self.last:
			return None
		return self.tokens[self.index]

	def peek(self):
		# Return the next token without moving.
		if self.index + 1 >= self.last:
			return None
		return self.tokens[self.index + 1]
		
	def move(self):
		self.index += 1

	def parse_atom(self):
		# An atom is a number, a string,
		# anything that can't really be
		# divided further.

		# We read the next avaliable token
		n = self.next()
		if not n:
			raise Exception("Unexpected End Of File")
		
		if n.type == "number":
			# We return a numer node with the
			# value of the token. 
			return NumberNode(int(n.value))
		elif n.type == "opening":
			# We have an opening parenthesis!
			# We should parse an expression then.
			return self.parse_expr()
		else:
			# we don't have an atom!
			raise Exception("Expected an atom!")

	def parse_mul_div(self):
		# go down to parse_add_sub() first!

		# We parse atoms instead of mul/div here
		n = self.parse_atom()
		token = self.peek()
		
		if not token: return n
		
		while token.type == 'multiply' or token.type == 'divide':
			self.move()
			n = OperationNode(token.type, n, self.parse_atom())
			token = self.peek()
			if not token: break

		return n
	
	def parse_add_sub(self):
		# Here we parse addition and substraction.
		# Example: 1 + 2 + 3

		# First, read a mul/div.
		# 1 + 2 + 3
		# ^
		n = self.parse_mul_div()

		# Have a look at the next token
		# 1 + 2 + 3
		# ~ ^
		token = self.peek()

		# Just a number is a valid
		if not token: return n

		# add/sub expression!
		while token.type == 'add' or token.type == 'substract':
			# '+' has indeed type 'add'
			self.move()
			# 1 + 2 + 3
			#     ^
			
			# This is the hard part basically
			n = OperationNode(token.type, n, self.parse_mul_div())
			
			token = self.peek()
			if not token: break

		return n

		#* n= 1
		# First iteration of the while loop:
		#* n=  (+)
		#*    /  \
		#*   1   ..
		# mul/div:
		#* n=  (+)
		#*    /  \
		#*   1   2

		# Next iteration of the while loop:
		#* n=     (+)
		#*       /   \
		#*     (+)   ..
		#*    /  \
		#*   1   2
		# mul/div:
		#* n=     (+)
		#*       /   \
		#*     (+)   3
		#*    /  \
		#*   1   2

		
	
	def parse_expr(self):
		return self.parse_add_sub()

tokens = lex("1 + 2")
print("Tokens:", tokens)
p = Parser(tokens)
n = p.parse_expr()
n.print()


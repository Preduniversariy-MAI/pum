from testing.parsing import *

# Evaluating or Interpreting the code.
# Basically we have a recursive function
# that goes over the AST and evaluates a
# single node, returning some kind of object.
# We only have numbers in our "language"
# so there is only one object type.

def evaluate(node: Node) -> int:
	if not node:
		raise Exception("The node is None!")
	
	# We have a number node:
	if isinstance(node, NumberNode):
		# Simple, we return a number
		return node.value

	elif isinstance(node, OperationNode):
		# Interesting part here:
		# We evaluate the child nodes
		# and get their result.
		lhs, rhs = evaluate(node.left), evaluate(node.right)

		# Check the operation type and
		# do it accordingly
		if node.type == "add":
			return lhs + rhs
		elif node.type == "substract":
			return lhs - rhs
		elif node.type == "multiply":
			return lhs * rhs
		elif node.type == "divide":
			return lhs / rhs
		else:
			raise Exception("Unknown operation type: " + node.type)

if __name__ == "__main__":
	inp = input("Input your exression: ")
	tokens = lex(inp)
	print("Tokens:", tokens)

	p = Parser(tokens)
	n = p.parse_expr()
	n.print()

	r = evaluate(n)
	print("Result:", r)

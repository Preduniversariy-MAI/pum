# The virtual machine.
# Basically the same as your normal
# computer processsor, but with more
# abstractions and features.

# Our virtual machine is stack-based,
# meaning that the primary way of storing
# and evaluating information is using a stack.
# 
# But what is a *Stack*?
# Imagine a box!
#* \     /
#* |     |
#* |     |
#* |     |
#* |     |
#* |_____|
# You can put (for example) numbers in that box:  
#* \     /
#* |  3  |
#* | 271 |
#* |  8  |
#* | 12  |
#* |_____|
# But only on top of the previous number
# And you can take numbers from that box:
#* \     /
#* |     |
#* | 271 |
#* |  8  |
#* | 12  |
#* |_____|
# But only from the top of the box!
# Well, a stack is like this box.
# Putting something in the box is called *pusing on the stack*
# Taking something from the box is called *popping from the stack*


from testing.evaluating import evaluate
from testing.compiling.bytecode import *


class VM:
	def __init__(self, instrs: list[Instr]):
		self.instrs = instrs
		self.stack: list[int] = []
	
	# Push on the stack:
	def push(self, number: int):
		self.stack.append(number)

	# Pop from the stack:
	def pop(self) -> int:
		return self.stack.pop()

	# The last element int the stack:
	def top(self) -> int:
		return self.stack[-1]

	def run(self):
		for i in self.instrs:
			self.evaluate(i)
		return self.top()

	def evaluate(self, instr: Instr):
		if instr.type == "number":
			if len(instr.args) != 1:
				raise Exception("Invalid instruction arguments. (" + instr.type + ')')
			# The number instruction.
			# We push the number onto the stack.
			self.push(instr.args[0])

		elif instr.type == "add":
			if len(instr.args) != 0:
				raise Exception("Invalid instruction arguments. (" + instr.type + ')')
			# Adding!
			# First we pop the right hand side from the stack
			rhs = self.pop()
			# And then the left hand side
			lhs = self.pop()
			# Now we push the result:
			self.push(lhs + rhs)

		elif instr.type == "substract":
			if len(instr.args) != 0:
				raise Exception("Invalid instruction arguments. (" + instr.type + ')')
			rhs, lhs = self.pop(), self.pop()
			self.push(lhs - rhs)

			
		elif instr.type == "multiply":
			if len(instr.args) != 0:
				raise Exception("Invalid instruction arguments. (" + instr.type + ')')
			rhs, lhs = self.pop(), self.pop()
			self.push(lhs * rhs)

			
		elif instr.type == "divide":
			if len(instr.args) != 0:
				raise Exception("Invalid instruction arguments. (" + instr.type + ')')
			rhs, lhs = self.pop(), self.pop()
			self.push(lhs / rhs)

		else:
			raise Exception("Invalid instruction: " + instr.type)

if __name__ == "__main__":
	import testing.lexing as L
	import testing.parsing as P
	import testing.compiling.compiling as C
	inp = input("Input your exression: ")
	tokens = L.lex(inp)
	print("Tokens:", tokens)

	p = P.Parser(tokens)
	n = p.parse_expr()
	n.print()

	c = C.Compiler()
	c.compile(n)
	i = c.instr
	print("Instructions: ", i)

	v = VM(i)
	print("Result:",v.run())

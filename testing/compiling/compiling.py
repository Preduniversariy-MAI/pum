# When compiling, we do pretty
# much the same as when interpreting
# (Same going over a tree and doing something)
# but instead of returning a number,
# we generate code in some other language!
# (for example, in C or assembly)
# In our case, we will be generating
# something called *Bytecode*
# Bytecode is similar to machine code
# but instead of the processor running it,
# we have a Virtual Machine.
# A Virtual Machine goes over the instructions
# supplied to it and runs them.

# Our virtual machine is stack-based.
# have a look in vm.py for more detail

from testing.compiling.bytecode import *
from testing.parsing import *

class Compiler:
	instr: list[Instr]
	def __init__(self):
		self.instr = []

	def compile(self, node: Node) -> None:

		# if the node is a number, we output
		# a `number` instruction.
		if isinstance(node, NumberNode):
			self.instr.append(Instr("number", node.value))

		elif isinstance(node, OperationNode):
			# First we output the child nodes.
			self.compile(node.left)
			self.compile(node.right)
			# then the instruction inself.
			self.instr.append(Instr(node.type))
		
		else:
			raise Exception("Unknown node: " + node.__class__.__name__)

# How instructions look:
#* opcode param1 param2 ...

# An Opcode or Operation Code
# is a number telling the VM
# or the processor what operaion to do.
OPCODES = [
	"add",
	"substract",
	"multiply",
	"divide",
	"number",
]

# An instruction:
class Instr:
	def __init__(self, type: str, *args: int):
		if type not in OPCODES:
			raise KeyError("Wrong instruction type: " + type)
		self.type = type
		self.args = args

	def __repr__(self):
		if self.args:
			return f"Instr(" + self.type + ': ' + ', '.join(map(str, self.args)) + ")"
		else:
			return f"Instr(" + self.type + ")"


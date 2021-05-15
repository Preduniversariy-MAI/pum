# Parsing.
# One of the most hard to understand
# parts of a programming langage!

# Take for example a simple
# mathematical expression:

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
# Note: (+) could acutally have more
# child nodes, but it is harder to
# implement (we might do that actually)

# Now! how do we convert 1 + 2 into a tree?
# I will be going over top-down parsing.
# This is where the lexer comes in.



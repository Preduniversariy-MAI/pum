# Actual extension is .pum but .py gives syntax highlighting
# Idea #1

print "Hello, World!"
# I am not sure if I should add or remove parentheses for function calls.
# We could do
print [1, 2, 3, 4].2 #=> 3
a = 3
print [1, 2, 3, 4].(a) #=> a


#==============================================#
# An example of the standart library
print ([1, 2, 3, 4].map str).joined_by ', '

#==============================================#

# Another way of using this syntax is:
print [1, 2, 3, 4].(map str).joined_by ', '
# But this is less clear.

#==============================================#

# This may be used.
print [1, 2, 3, 4](.map str).joined_by ', '
# To allow such syntax the parser shouldn't parse
a b(c).d, e
# as a(b(c).d, e), instead it should be parsd as
# a (b c).e, d
# where b c is a direct concatenation of b and c.
# so if c was (.func args) it should be
# a (b.func args), d
# if c was (+ 3) the result would be
# a (b + 3), d

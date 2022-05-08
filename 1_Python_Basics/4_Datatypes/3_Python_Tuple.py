# Tuple is an ordered sequence of items same as a list.
# The only difference is that tuples are immutable.
# Tuples once created cannot be modified
t = (5, 'program', 1+3j)

# t[1] = 'program'
print("t[1] = ", t[1])

# t[0:2] = [5, 'program']
print("t[0:2] = ", t[0:2])

# Generate error
# Tupes are immutable
t[0] = 10
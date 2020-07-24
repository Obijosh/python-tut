# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods.
name = 'Joshua'
age = 20

# Concatenate
print ( 'Hello, my name is as you all know ' + name + ' and i am you know the digit ' + str (age) + ' that is actually my age')

# String Formatting

# Arguments by Position
print ( 'My name is {name} and i am {age} ' . format (name=name, age=age))

# F_Strings (3.6+)
print (f'Hello, my name is {name} and i am {age}')

# String Methods

s = 'helloworld'

# Capitalize String
print (s.capitalize ())

# Make all uppercase
print (s.upper())

# Make all Lower
print (s.lower())

# Swap Case
print (s.swapcase())

# Get Length
print (len(s))

# Replace
print (s.replace ('world', 'everyone'))

# Count
sub = 'h'
print (s.count (sub))

# Starts With
print (s.startswith ('hello'))

#Ends With
print (s.endswith ('d'))

# Split into a list
print (s.split())

# Find Position
print (s.find ('r'))

# Is all alphanumeric
print (s.isalnum ())

# Ia all alphebetic
print (s.isalpha ())

# Is all numeric
print (s.isnumeric ())

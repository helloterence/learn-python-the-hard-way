# Initialize x to the string 'There are 10 types of people.'
x = "There are %d types of people." % 10

# Initialize binary to the string 'binary'
binary = "binary"

# Initialize do_not to the string "don't"
do_not = "don't"

# Initialize y to the string "Those who know binary and those who don't"
y = "Those who know %s and those who %s" % (binary, do_not)

# Print "There are 10 types of people."
print x 

# Print "Those who know binary and those who don't"
print y

# Print "I said: 'There are 10 types of people.'."
print "I said: %r." % x

# Print "I also said: 'Those who know binary and those who don't'."
print "I also said: '%s'." % y

# Initialize hilarious to False
hilarious = False

# Initialize joke_evaluation to the string "Isn't that joke so funny?! %r"
joke_evaluation = "Isn't that joke so funny?! %r"

# Print "Isn't that joke so funny?! False"
print joke_evaluation % hilarious

# Initialize w to the string "This is the left side of..."
w = "This is the left side of..."

# Initialize e to the string "a string with a right side."
e = "a string with a right side."

# Concatenate w and e
print w + e
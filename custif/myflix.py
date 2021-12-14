#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""


message = 'What  your dog says about you.  '

# wrap connection in a float() to accept decimals as numbers
dogbreed = str(input("What is your dogs breed?"))

# if input value was higher or equal to 25
if dogbreed == bulldog:
    message = message + 'You are a tuff guy.'
elif dogbreed == poodle:
    message = message + 'Very pretty princess.'
elif connection >= 2:
    message = message + 'setting video to 720p.'
else:
    message = message + 'finding another access network.'
print(message)


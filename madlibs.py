#create a madlibs game
#prompt user for inputs
color = input("Enter a color: ")
plural_noun =  input("Enter a plural noun: ")
message = input("Enter a message: ")
#printing out a new line before we print out the input as desired
print()

#print out inputs as expected using the format specifier
print(f"Roses are {color}")
print(f"{plural_noun} are {color}")
print(f"I love {message}")
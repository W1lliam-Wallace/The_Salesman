from time import *


def rules():
    print()
    # Rules go here


print("\nTHE SALESMAN")
sleep(1.5)
read_rules = input("Would you like to read the rules (yes/no)? ")
if read_rules.lower() == "yes":
    rules()
    # Function containing the rules
elif read_rules.lower() == "no":
    print()
    # Skips straight to next line of code
else:
    print("I'm sorry, I did not understand that request")
    # Loop back to beginning ask again


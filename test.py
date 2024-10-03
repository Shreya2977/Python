# Python code to check validity of mobile number (Long Code)
#sys.exit([arg]):
# This function is used to exit the program.
# You can provide an optional argument, which can be an integer (exit code) or another object like a string to describe the reason for exiting.

# import sys

# number = input("Enter the mobile number: ")

# # Check if the length is not 10 digits
# if len(number) != 10:
#     print('Invalid')
#     sys.exit(0)

# # Check if the number starts with '0'
# if number[0] == '0':
#     print('Invalid')
#     sys.exit(0)

# # Check if all characters are digits
# if not number.isdigit():
#     print('Invalid')
# else:
#     print('Valid')

# import re
# if re.match("..$","fi"):
#     print("Matched")
# else:
#     print("Not matched")

# import re
# if re.match("..","fooo"):
#     print("Matched")
# else:
#     print("Not matched")

# import re
# if re.match(".end","bend hi all"):
#     print("Matched")
# else:
#     print("Not matched")
# import re
# if re.match("end.$","all the ends best bends"):
#     print("Matched")
# else:
#     print("Not matched")

import re
pan=input()
print(len(pan))
if len(pan)<10 or len(pan)>10:
    print ("PAN Number should be 10 characters")
    exit
elif re.search("[^a-zA-Z0-9]",pan):
    print ("No symbols allowed, only alphanumerics")
    exit
elif re.search("[0-9]",pan[0:5]):
    print ("Invalid - 1")
    exit
elif re.search("[A-Za-z]",pan[5:9]):
    print ("Invalid - 2")
    exit
elif re.search("[0-9]",pan[-1]):
    print ("Invalid - 3")
    exit
else:
    print ("Your card "+ pan + " is valid")
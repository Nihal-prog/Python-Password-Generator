# Strong Password Generator

# Importing Modules Required
import string
import random
import pyfiglet as pf

# Banner
banner = pf.figlet_format("Password Generator")
print(banner)

# Main Code
if __name__ == "__main__":

    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    plen = int(input("Enter the Length of Password : "))

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    print("Your Password is :")
    print("".join(s[0:plen]))

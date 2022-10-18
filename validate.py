# re library(some usefull stuff.)
#       . ----> any character except a newline.
#       * ----> 0 or more repetitions.
#       + ----> 1 or more repetitions.
#       ? ----> 0 or 1 repetitions.
#       {m} ----> m repetitions.
#       {m,n} ----> m-n repetitions.  
#       [] ----> set of characters.
#       [^] ----> complementing the set.   
#       ^ ----> matches the start of the string.
#       $ ----> matches the end of the string or just before the newline at the end of the string.


import re

email = input("Enter your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.(com|edu|gov|net|org)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid!")
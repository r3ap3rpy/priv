import privy
from getpass import getpass

password = getpass("Enter the pass for encrypt:")

data = b"This is the top secret!" 

hidden = privy.hide(data, password)

print(hidden)

unhidden = privy.peek(hidden, password)

print(unhidden)

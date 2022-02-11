import privy
from getpass import getpass

password = getpass("Enter password:")

data = b"This is the secret!"

with open("hidden","wb") as hidden_file:
    hidden_file.write(privy.hide(data,password).encode())
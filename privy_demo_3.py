import privy
from getpass import getpass

password = getpass("Enter password:")

with open("hidden","rb") as hidden_file:
    print(privy.peek(hidden_file.read(),password))
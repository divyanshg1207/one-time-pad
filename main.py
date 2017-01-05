import sys
from takeinput import takeinput
import crypt

inp = sys.argv

order,directory,key_directory= takeinput(inp)

if order=="encrypt":
    try:
        crypt.encrypt(directory,key_directory)
        print("Encrypted")
    except:
        print("error during encryption")
    
elif order=="decrypt":
    try:
        crypt.decrypt(directory,key_directory)
        print("Decrypted")
    except:
        print('error during decryption')
else:
    print("error: can't understand input")


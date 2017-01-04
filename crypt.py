def encrypt(directory,key_directory):
    with open(key_directory,'r') as f:
        key = f.read().strip()
    with open(directory,'r') as f:
        message = f.read().strip()
    
    index = 0
    string = ''
    aindex = ord('a') - 1
    Aindex = ord('A') - 1

    for i in message:
        if i.isalpha():
            
            if key[index].islower():
                shift = ord(key[index]) - aindex
            else:
                shift = ord(key[index]) - Aindex
                
            char = ord(i) + shift
            
            if i.islower():
                if char > ord('z'):
                    char -= 26
            else:
                if char > ord('Z'):
                    char -= 26

            string += chr(char)
       
        else:
            string += i

        index += 1
        if index==len(key):
            index = 0
        
    with open(directory+'.encrypt','x') as f:
        f.write(string)
        
def decrypt(directory,key_directory):
    with open(key_directory,'r') as f:
        key = f.read().strip()
    with open(directory,'r') as f:
        message = f.read().strip()

    index = 0
    string = ''
    aindex = ord('a')-1
    Aindex = ord('A')-1
    
    for i in message:
        if i.isalpha():
            if key[index].islower():
                shift = ord(key[index]) - aindex
            else:
                shift = ord(key[index]) - Aindex

            char = ord(i) - shift

            if i.islower():
                if char < ord('a'):
                    char += 26
            else:
                if char < ord('A'):
                    char += 26
                    
            string += chr(char)

        else:
            string += i

        index += 1
        
        if index==len(key):
            index = 0
            
    if directory[-8:]==".encrypt":
        directory = directory[:-8]+'.decrypt'
    with open(directory,'x') as f:
        f.write(string)

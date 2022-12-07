from Stegano.hide import encode
from Stegano.reveal import decode
from Crypto.encrypt import encrypt
from Crypto.decrypt import deccrypt



def charlist(begin, end):
    charlist = []
    for i in range(begin, end):
        if(chr(i) != ' ' and chr(i) != '_'):
            charlist.append(chr(i))
    return ''.join(charlist)


_encoded = charlist(0,200)

# for Steganography
# encode(_encoded, "hide")
# _decoded = decode("hide")

# if(_encoded == _decoded):
#     print("It Works!")
# else:
#     print("Booooo")

# for Cryptography
# cipher = encrypt(_encoded)
# decipher = deccrypt(cipher)

# if(_encoded == decipher):
#     print("It Works!")
# else:
#     print("Booooo")
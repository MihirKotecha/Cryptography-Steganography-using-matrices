from Stegano.hide import encode
from Stegano.reveal import decode

def charlist(begin, end):
    charlist = []
    for i in range(begin, end):
        charlist.append(chr(i))
    return ''.join(charlist)


_encoded = charlist(0,200)

# Assigning
encode(_encoded, "hide")
_decoded = decode("hide")

if(_encoded == _decoded):
    print("It Works!")
else:
    print("Booooo")
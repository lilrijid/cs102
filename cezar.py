
def encrypt_caesar(plaintext):
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("")
    ''
    """

    ciphertext = ''
    for element in plaintext:
        if 97 <= (ord(element) + 3) <= 122 or 65 <= (ord(element) + 3) <= 90:
            ciphertext += chr(ord(element) + 3)
        elif 122 < (ord(element) + 3) <= 125 or 90 < (ord(element) + 3) <= 93:
            ciphertext += chr(ord(element) - 26 + 3)
        else:
            ciphertext += element
    return ciphertext


def decrypt_caesar(ciphertext):
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for ttl in ciphertext:
        if (97 <= (ord(ttl) - 3) <= 122) or (65 <= (ord(ttl) - 3) <= 90):
            plaintext += chr(ord(ttl) - 3)
        elif (94 <= (ord(ttl) - 3) < 97) or (62 <= (ord(ttl) - 3) < 65):
            plaintext += chr(ord(ttl) + 26 - 3)
        else:
            plaintext += ttl
    return plaintext

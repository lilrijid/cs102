def encrypt_vigenere(plaintext, keyword):
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    small = keyword.lower()
    ciphertext = ""
    a = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(plaintext)):
        ind = ord(plaintext[i])
        search = a.find(small[i % len(small)])
        if (97 <= ind <= 122):
            if (97 <= ind + search <= 122):
                ciphertext += chr(ind + search)
            else:
                ciphertext += chr(ind + search - 26)
        elif (65 <= ind <= 90):
            if (65 <= ind + search <= 90):
                ciphertext += chr(ind + search)
            else:
                ciphertext += chr(ind + search - 26)
        else:
            ciphertext += plaintext[i]
    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    small = str(keyword).lower()
    plaintext = ""
    a = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(str(ciphertext))):
        ind = ord(str(ciphertext)[i])
        search = a.find(small[i % len(small)])
        if (97 <= ind <= 122):
            if (97 <= ind - search <= 122):
                plaintext += chr(ind - search)
            else:
                plaintext += chr(ind - search + 26)

        elif (65 <= ind <= 90):
            if (65 <= ind - search <= 90):
                plaintext += chr(ind - search)
            else:
                plaintext += chr(ind - search + 26)
        else:
            plaintext += str(ciphertext)[i]
    return plaintext


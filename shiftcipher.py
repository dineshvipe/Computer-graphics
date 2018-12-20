def encrypt(letter, key):

    # must be single alphabetic character
    if not letter.isalpha() or len(letter) != 1:
        return letter

    # convert to lowercase
    letter = letter.lower()

    # convert to numerical value 0 - 25
    # a = 0, b = 1, ... z = 25
    value = ord(letter) - 97

    # apply key, number of characters to shift
    value = (value + key) % 26

    # return encrypted letter
    return chr(value + 97)


def decrypt(letter, key):

    # must be single alphabetic character
    if not letter.isalpha() or len(letter) != 1:
        return letter

    # convert to lowercase
    letter = letter.lower()

    # convert to numerical value 0 - 25
    # a = 0, b = 1, ... z = 25
    value = ord(letter) - 97

    # apply key, number of characters to shift
    value = (value - key) % 26

    # return encrypted letter
    return chr(value + 97)


# number of characters to shift
key = int(input('Enter the secret key: '))

# cipher
print('cipher ( {} )\n'.format(key))
for letter in map(chr, range(97, 123)):
    print('{} -> {}'.format(letter, encrypt(letter, key)))
print ('')

# message to encrypt
plaintext = input('Enter the plaintext message: ')
print('plaintext: {}\n'.format(plaintext))

# encipher
ciphertext = ''
for letter in plaintext:
    ciphertext += encrypt(letter, key)
print('ciphertext: {}\n'.format(ciphertext))

# decipher
plaintext2 = ''
for letter in ciphertext:
    plaintext2 += decrypt(letter, key)
print('Decrypted plaintext: {}'.format(plaintext2))

"""
    OUTPUT
    Enter the secret key: 4
    Enter the plaintext message: dinesh
    plaintext: dinesh
    ciphertext: hmriwl
    Decrypted plaintext: dinesh
"""
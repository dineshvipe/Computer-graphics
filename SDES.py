key = "0111111101"
cipher = "10100010"


P10 = (3, 5, 2, 7, 4, 10, 1, 9, 8, 6)
P8 = (6, 3, 7, 4, 8, 5, 10, 9)
P4 = (2, 4, 3, 1)

IP = (2, 6, 3, 1, 4, 8, 5, 7)
IPi = (4, 1, 3, 5, 7, 2, 8, 6)

E = (4, 1, 2, 3, 2, 3, 4, 1)

S0 = [
        [1, 0, 3, 2],
        [3, 2, 1, 0],
        [0, 2, 1, 3],
        [3, 1, 3, 2]
     ]

S1 = [
        [0, 1, 2, 3],
        [2, 0, 1, 3],
        [3, 0, 1, 0],
        [2, 1, 0, 3]
     ]

def permutation(perm, key):
    permutated_key = ""
    for i in perm:
        permutated_key += key[i-1]
        #print(permutated_key,key)

    print(permutated_key)

    return permutated_key

def generate_first_key(left_key, right_key):
    left_key_rot = left_key[1:] + left_key[:1]
    right_key_rot = right_key[1:] + right_key[:1]
    key_rot = left_key_rot + right_key_rot
    return permutation(P8, key_rot)

def generate_second_key(left_key, right_key):
    left_key_rot = left_key[3:] + left_key[:3]
    right_key_rot = right_key[3:] + right_key[:3]
    key_rot = left_key_rot + right_key_rot
    return permutation(P8, key_rot)

def F(right, subkey):
    expanded_cipher = permutation(E, right)
    print("Expanded cipher: {}".format(expanded_cipher))
    xor_cipher = bin( int(expanded_cipher, 2) ^ int(subkey, 2) )[2:].zfill(8)
    print("XOR Result with Key and Expanded cipher: {}".format(xor_cipher))
    left_xor_cipher = xor_cipher[:4]
    right_xor_cipher = xor_cipher[4:]
    left_sbox_cipher = Sbox(left_xor_cipher, S0)
    print("S-Box for Left: {}".format(left_sbox_cipher))
    right_sbox_cipher = Sbox(right_xor_cipher, S1)
    print("S-Box for Right: {}".format(right_sbox_cipher))
    op_with_p4=permutation(P4, left_sbox_cipher + right_sbox_cipher)
    print("Addition of left and right S-Box and permutation with P4: {}".format(op_with_p4))
    return op_with_p4

def Sbox(input, sbox):
    row = int(input[0] + input[3], 2)
    column = int(input[1] + input[2], 2)
    return bin(sbox[row][column])[2:].zfill(4)

def f(first_half, second_half, key):
    left = int(first_half, 2) ^ int(F(second_half, key), 2)
    print ("First Xor: " + bin(left)[2:].zfill(4) + second_half)
    return bin(left)[2:].zfill(4), second_half

def decryption(ciphertext,key):
    pass

p10key = permutation(P10, key)
left = p10key[:len(p10key)//2]
right = p10key[len(p10key)//2:]

first_key = generate_first_key(left, right)
second_key = generate_second_key(left, right)
print ("First key: " + first_key)
print ("Second key: " + second_key)

permutated_cipher = permutation(IP, cipher)
print ("Permuted IP: " + permutated_cipher)
first_half_cipher = permutated_cipher[:len(permutated_cipher)//2]
second_half_cipher = permutated_cipher[len(permutated_cipher)//2:]

left, right = f(first_half_cipher, second_half_cipher, second_key)
print ("return from left+right: " + right + left)
left, right = f(right, left, first_key) # switch left and right!
text=permutation(IPi, left + right)
print("IP^-1 or Final CipherText    : " + text)
key0,key1=second_key,first_key
first_half_cipher = text[:len(text)//2]
second_half_cipher = text[len(text)//2:]
left, right = f(first_half_cipher, second_half_cipher, key1)
left, right = f(right, left, first_key)
text=permutation(IPi, left + right)
print("\nDecrypted text: {}".format(text))

"""
OUTPUT

1111110011
01011111
11111100
First key: 01011111
Second key: 11111100
00110001
Permuted IP: 00110001
10000010
Expanded cipher: 10000010
XOR Result with Key and Expanded cipher: 01111110
S-Box for Left: 0000
S-Box for Right: 0000
0000
Addition of left and right S-Box and permutation with P4: 0000
First Xor: 00110001
return from left+right: 00010011
10010110
Expanded cipher: 10010110
XOR Result with Key and Expanded cipher: 11001001
S-Box for Left: 0001
S-Box for Right: 0010
0100
Addition of left and right S-Box and permutation with P4: 0100
First Xor: 01010011
10001110
IP^-1 or Final CipherText    : 10001110
01111101
Expanded cipher: 01111101
XOR Result with Key and Expanded cipher: 00100010
S-Box for Left: 0000
S-Box for Right: 0001
0000
Addition of left and right S-Box and permutation with P4: 0000
First Xor: 10001110
01000001
Expanded cipher: 01000001
XOR Result with Key and Expanded cipher: 00011110
S-Box for Left: 0011
S-Box for Right: 0000
0110
Addition of left and right S-Box and permutation with P4: 0110
First Xor: 10001000
Decrypted text: 01011111
"""
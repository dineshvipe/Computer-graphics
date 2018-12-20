import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def multiplicative_inverse(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    
    n = p * q

    
    phi = (p-1) * (q-1)

    e = random.randrange(12, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(12, phi)
        g = gcd(e, phi)

    
    d = multiplicative_inverse(e, phi)
    
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    key, n = pk
    
    cipher = [(ord(char) ** key) % n for char in plaintext]
    
    return cipher

def decrypt(pk, ciphertext):
    
    key, n = pk
    
    plain = [chr((char ** key) % n) for char in ciphertext]
    
    return ''.join(plain)
    

if __name__ == '__main__':
    
    p = int(input("\nEnter a prime number (17, 19, 23, etc): "))
    q = int(input("\nEnter another prime number (Not one you entered above): "))
    
    print("\nGenerating your public/private keypairs now . . .")
    
    public, private = generate_keypair(p, q)
    
    print ("\nYour public key is ", public ," and your private key is ", private)
    
    message = input("\nEnter a message to encrypt with your private key: ")
    encrypted_msg = encrypt(private, message)
    
    print("\nYour encrypted message is: {}".format(''.join(map(lambda x: str(x), encrypted_msg))))
    print ("\nDecrypting message with public key ", public ," . . .")
    print ("\nYour message is: {}".format(decrypt(public, encrypted_msg)))


    """
    OUTPUT

    
Enter a prime number (17, 19, 23, etc): 7

Enter another prime number (Not one you entered above): 13

Generating your public/private keypairs now . . .

Your public key is  (25, 91)  and your private key is  (49, 91)

Enter a message to encrypt with your private key: dinesh

Your encrypted message is: 91419102413

Decrypting message with public key  (25, 91)  . . .

Your message is:        ♫‼
↑


Enter a prime number (17, 19, 23, etc): 7

Enter another prime number (Not one you entered above): 23

Generating your public/private keypairs now . . .

Your public key is  (43, 161)  and your private key is  (43, 161)

Enter a message to encrypt with your private key: dinesh

Your encrypted message is: 721541248711548

Decrypting message with public key  (43, 161)  . . .

Your message is: dinesh
    """
import random
import string
import sys

def encrypt(msg, key):
	
	msg = msg.replace(' ', '')
	while len(msg) % len(key) != 0:
		msg += random.choice(string.ascii_uppercase)
	chunks = [msg[i:i+len(key)] for i in range(0, len(msg), len(key))]
	order = [''.join(sorted(key)).find(x) for x in key]
	x = map(lambda k: [c for (y,c) in sorted(zip(order, k))], chunks)
	result = [l[i] for i in range(len(key)) for l in x]
	result = ''.join(result)
	return result

def decrypt(msg, key):
	order = [key.find(x) for x in sorted(key)]
	chunks = [msg[k+x*len(msg)//len(key)] for k in range(len(msg)//len(key)) for x in range(len(key))]
	chunks = [chunks[i:i+len(key)] for i in range(0, len(chunks), len(key))]
	x = map(lambda k: ''.join([c for (y,c) in sorted(zip(order, k))]), chunks)
	return ''.join(x)

if __name__ == '__main__':
	key=input("Enter The Key: ")
	st=input("Enter The String: ")
	print("--------------ENCRYPTING--------------------")
	e1=encrypt(st,key)
	key2="Zebras"
	print("Encrypted Text for single: {}".format(e1))
	e2=encrypt(e1,key2)
	print("Encrypted Text for Double: {}".format(e2))
	print("---------------Decrypting--------------------")
	e3=decrypt(e2,key2)
	print("First Round Decrypted: {}".format(e3))
	print("FInal Decrypted Text: {}".format(decrypt(e3,key)))
	print("-----------------------------------------------")

	"""
		OUTPUT

	Enter The Key: rebar
	Enter The String: noonei
	--------------ENCRYPTING--------------------
	Encrypted Text for single: ENOONI
	Encrypted Text for Double: NONOIE
	---------------Decrypting--------------------
	First Round Decrypted:enooni
	FInal Decrypted Text: noonei
	-----------------------------------------------
import random 
import socket,pickle

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',8000))
s.listen(1)
data,addr=s.accept()
print("Got connection from Addr: {}".format(addr))
p,g=input("Enter The public key: ").split()
if(is_prime(int(p))):
    a=random.randrange(10,99)
    x=int(g)**a%int(p)
    l=[int(p),int(g),int(x)]
    print("Sending data: {}".format(l))
    lt=pickle.dumps(l)
    #print(lt)
    data.send(lt)
    y=data.recv(1000)
    if(y!=None):
        ka=int(y)**a%int(p)
        print("Secret Key: {}".format(ka))
    s.close()

CLIENT Program

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',8000))
d=s.recv(10000)
dd=pickle.loads(d)
print("Recieved: {}".format(dd))
#print(d[0][2:],int(d[1],int(d[2]),int(d[3])))
b=random.randrange(10,99)
y=int(dd[1])**b%int(dd[0])
y=str(y)
s.send(y.encode('ascii'))
kb=int(dd[2])**b%int(dd[0])
print("Key Formed: {}".format(kb))


"""
OUTPUT

SERVER: 
Got connection from Addr: ('127.0.0.1', 11571)
Enter The public key: 107 43
Sending data: [107, 43, 70]
Secret Key: 25

CLIENT:
Recieved: [107, 43, 70]
Key Formed: 25

"""
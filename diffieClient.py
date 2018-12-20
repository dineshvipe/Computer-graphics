import random,socket
import pickle
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

#print(int(d)**2)

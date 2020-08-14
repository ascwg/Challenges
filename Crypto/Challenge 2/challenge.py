from Crypto.Cipher import AES
import base64
from string import printable
import random


BLOCK_SIZE = 16

pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)

unpad = lambda s: s[:-ord(s[len(s) - 1:])]

def encrypt(plain, key):
    plain = pad(plain)
    cipher = AES.new(key, AES.MODE_ECB)
    return base64.b64encode(cipher.encrypt(plain))

def generate_random():
    letters = printable
    temp = []
    for i in range(4):
        temp.append(''.join(random.choice(letters) for i in range(1)))
    
    return "".join(temp)
def choose_random(length=1):
    letters = printable
    a = ''.join(random.choice(letters) for i in range(length))
    b = ''.join(random.choice(letters) for i in range(length))
    b = a+b
    return b


all_keys = []
for i in range(8):
    all_keys.append(choose_random(1))




plain = base64.b64encode(open("temp.txt").read()).encode("hex")

c1 = encrypt(plain, all_keys[0]*8).encode("hex")

c2 = encrypt(c1, all_keys[1]*8).encode("hex")

c3 = encrypt(c2, all_keys[2]*8).encode("hex")

c4 = encrypt(c3, all_keys[3]*8).encode("hex")

c5 = encrypt(c4, all_keys[4]*8).encode("hex")

c6 = encrypt(c5, all_keys[5]*8).encode("hex")

c7 = encrypt(c6, all_keys[6]*8).encode("hex")

c8 = encrypt(c7, all_keys[7]*8).encode("hex")

random = generate_random()

c9 = encrypt(c8,random*4).encode("hex")

print "temp = ", c9

key = ""
for i in all_keys:
    key = key + i

flag = open("flag.txt").read()

cipher = encrypt(flag, key).encode("hex")

print "cipher = ",cipher

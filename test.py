# coding: utf-8
import hashlib

#def sha0(msg): return int(hashlib.sha256(msg).hexdigest()[0:2], 16)

print (hashlib.sha256("wolfcryptrocks".encode('utf-8')).hexdigest())
#print (sha0('wolfcryptrocks'.encode('utf-8')))
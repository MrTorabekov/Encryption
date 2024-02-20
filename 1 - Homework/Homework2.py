# Homework 2

import rsa


(publickey, privatekey) = rsa.newkeys(1024)
# 
# print(f"this is public key -> {publickey}")
# print(f"this is private key -> {privatekey}")



# data = "Hi Torabekov_08".encode("utf-8")
# text = rsa.sign(data,privatekey,'SHA-1')
# rsa.verify(data,text,publickey)

data2 = "Hello world".encode("utf-8")
hash =rsa.compute_hash(data2 ,"SHA-1")

text2 = rsa.sign_hash(data2,privatekey,'SHA-1')
print(text2)
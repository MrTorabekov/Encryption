import rsa
# Homework 3

(publickey, privatekey) = rsa.newkeys(1024)

message = "Hi Torabekov_08".encode("utf-8")

ciphertext = rsa.encrypt(message, publickey)
dec_text = rsa.decrypt(ciphertext,privatekey)
# rsa.verify(message,ciphertext,publickey)

print(f"original data -> {message}")
print("")
print(f"heshlanga data -> {ciphertext}")
print("")
print(f"asliga qaytgan data -> {dec_text}")
print("")





data2 = "Hello world".encode("utf-8")
hash =rsa.compute_hash(data2 ,"SHA-1")
print(f"compute_hash -> {hash}")
print("")

text2 = rsa.sign_hash(hash,privatekey,'SHA-1')
print(f"sign_hash -> {text2}")

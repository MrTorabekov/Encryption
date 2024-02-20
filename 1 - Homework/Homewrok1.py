# • Cryptography Kutubxonasi orqali encrypted qilinga ma’lumotlarini decrypted qiling.
#
# • Endi o’zingiz musmustaqil Python RSA modulini yuklab Asimmetrik kalitli shifrlash ni amalga oshiring.
#
# • Asimmetrik kalitli shifrlash algoritim orqali encrypted qilinga ma’lumotni decrypted qilib ko’ring.






# Homework 1

from cryptography.fernet import Fernet

data = "Diyorbek"


key = Fernet.generate_key()

fernet = Fernet(key)

enc_data = fernet.encrypt(data.encode("utf-8"))
dec_data = fernet.decrypt(enc_data.decode("utf-8"))

print(f"Original text: {data}")
print(f"Encoded text: {enc_data}")
print(f"Decoded text: {dec_data}")
import base64

a = input("Malumot kiriting:")

password = a

encoded_data = base64.b64encode(password.encode("utf-8"))
dencoded_data = base64.b64decode(encoded_data.decode("utf-8")) # noqa

print(f"Original text: {password}")
print(f"Encoded text: {encoded_data}")
print(f"Decoded text: {dencoded_data}")
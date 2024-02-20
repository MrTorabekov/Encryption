from cryptography.fernet import Fernet

message = "Torabekov_08"

key = Fernet.generate_key()

fernet =Fernet(key)

encMessage = fernet.encrypt(message.encode())
decMessage = fernet.decrypt(encMessage.decode())

print(f"oldingi xabar: {message}")
print(f"heshlangan xabar: {encMessage}")
print(f"heshlanib kelgan xabar: {decMessage}")
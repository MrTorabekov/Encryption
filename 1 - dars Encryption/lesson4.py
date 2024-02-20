import base64

data = int(input(f"1 ecode\n2 decode\nsizga qaysi biri kerak tanlang:"))
password = input(f"Malumot kiriting:")



if data == 1:
    encoded_data = base64.b64encode(password.encode("utf-8"))
    print(encoded_data)
elif data == 2:
    decode_data = base64.b64decode(password.decode("utf-8"))
    print(decode_data)












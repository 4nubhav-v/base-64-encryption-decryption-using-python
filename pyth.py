import base64

a = int(input("Enter '1' for Encryption or '2' for Decryption :- "))


def encrypt_pass(password):
    encoded_bytes = base64.b64encode(password.encode())
    print(encoded_bytes)


def decrypt_pass(password):
    decoded_bytes = base64.b64decode(password)
    decoded_data = decoded_bytes.decode()
    print(decoded_data)


if a == 1:
    user_pass = input("Enter the password :- ")
    encrypt_pass(user_pass)
else:
    user_pass = input("Enter the encrypted password :- ")
    decrypt_pass(user_pass)

from cryptography.fernet import Fernet


message = input("enter  message to encode\n")
key = Fernet.generate_key()

fernet = Fernet(key)
print("original message\n",message)
d_cd = fernet.encrypt(message.encode())
print("encrypted message\n",d_cd)
d_ca = fernet.decrypt(d_cd).decode()
print("decrypted value\n",d_ca)
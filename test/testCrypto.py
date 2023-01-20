from cryptography.fernet import Fernet
  
# key is generated
# key = Fernet.generate_key()
key = b'chz4UshV2y2R3oCf_nWpX_PsqArGPy0WRrqE72krxbI='
print(key)
print(type(key))
  
# value of key is assigned to a variable
# f = Fernet(key)
  
# the plaintext is converted to ciphertext
token = Fernet(key).encrypt(b"welcome to geeksforgeeks")
  
# display the ciphertext
print(token)
  
# decrypting the ciphertext
d = Fernet(key).decrypt(token)
# for i in b:
#      c =c+chr(ord(i) ^ 0x01)
  
# display the plaintext
print(d)
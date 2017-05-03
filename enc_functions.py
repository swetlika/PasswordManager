from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import os

def rand_iv():
  return os.urandom(16)

def hash_pass(pw):
  hash = SHA256.new()
  hash.update(pw)
  return hash.digest()

def encrypt_msg(msg, pw):
  iv = rand_iv()
  key = hash_pass(pw)
  obj = AES.new(key, AES.MODE_CFB, iv)
  ciphertext = obj.encrypt(msg)
  #ciphertext = iv + ciphertext
  return iv,ciphertext
 
def decrypt_msg(ci, pw, iv):
  key = hash_pass(pw)
  obj = AES.new(key, AES.MODE_CFB, iv)
  return obj.decrypt(ci)

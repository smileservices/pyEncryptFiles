# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 21:53:56 2017
    About Fernet:
    https://cryptography.io/en/latest/fernet/

@author: vlad
"""
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def encrypt(path, password, salt):
    #get all files
    password = password.encode('utf-8')
    kdf = PBKDF2HMAC(
         algorithm=hashes.SHA256(),
         length=32,
         salt=salt,
         iterations=100000,
         backend=default_backend()
     )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    f = Fernet(key)
    with open(path, 'r+b') as content:
        token = f.encrypt(content.read())
        content.seek(0)
        content.write(token)

def decrypt(path, password, salt):
    #get all files
    password = password.encode('utf-8')
    kdf = PBKDF2HMAC(
         algorithm=hashes.SHA256(),
         length=32,
         salt=salt,
         iterations=100000,
         backend=default_backend()
     )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    f = Fernet(key)
    with open(path, 'rb') as content:
        decrypted = f.decrypt(content.read())
    with open(path, 'wb') as content:
        content.write(decrypted)

def doEncryption(path, password, salt):
    dirs = os.listdir(path)
    for file in dirs:
        file = path + file
        encrypt(file, password, salt)
        print('encrypted!')

def doDecryption(path, password, salt):
    dirs = os.listdir(path)
    for file in dirs:
        file = path + file
        decrypt(file, password, salt)
        print('decrypted!')
        
        
path = "path_to_folder"
password = input('Set encryption key: ')
salt = b'x\x86\xe1\xa8^i61\xaa\xe0:b\xb5\xde\xd9\xa3'

doEncryption(path, password, salt)
doDecryption(path, password, salt)
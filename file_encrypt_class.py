# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 21:53:56 2017
    About Fernet:
    https://cryptography.io/en/latest/fernet/

@author: vlad
"""
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class FileEncrypt(object):
    def __init__(self, password, salt):
        self.__password = password.encode('utf-8')
        self.__salt = salt

    def __setFernet(self):
        kdf = PBKDF2HMAC(
             algorithm=hashes.SHA256(),
             length=32,
             salt=self.__salt,
             iterations=100000,
             backend=default_backend()
         )
        key = base64.urlsafe_b64encode(kdf.derive(self.__password))
        self.__fernet = Fernet(key)

    def __encrypt(self, targetFile):
        self.__setFernet()
        with open(targetFile, 'r+b') as content:
            token = self.__fernet.encrypt(content.read())
            content.seek(0)
            content.write(token)

    def __decrypt(self, targetFile):
        self.__setFernet()
        with open(targetFile, 'rb') as content:
            decrypted = self.__fernet.decrypt(content.read())
        with open(targetFile, 'wb') as content:
            content.write(decrypted)

    def doEncryption(self, path):
        self.__encrypt(path)
        return True

    def doDecryption(self, path):
        self.__decrypt(path)
        return True
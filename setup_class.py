# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 21:53:56 2017
    About Fernet:
    https://cryptography.io/en/latest/fernet/

@author: vlad
"""
import os
from file_encrypt_class import FileEncrypt 

class Setup(object):

	def __init__(self):
		self.__setFolder()
		self.__setAction()
		self.__setSaltNPass()
		self.__getEncryptObj()

	def __getEncryptObj(self):
	    #initialize FileEncrypt Obj
	    encObj = FileEncrypt(
	                password=self.__password,
	                salt=self.__salt
	            )
	    self.__encryptObj = encObj

	def __setFolder(self):
		self.__folder = "C:/Users/vlad/Documents/PythonProjects/test_files"

	def __setAction(self):
		action = input('Select "e" for encrypt, "d" for decrypt, or "c" for cancel: ')
		if action not in ('e', 'd', 'c'): raise ValueError('What exactly do you want?')
		if action == 'c': exit()
		self.__action = action
		recur = input('Do selected action recursively? y/n: ')
		if recur == 'y': 
		    self.__recur = True 
		else:
		    self.__recur = False

	def __setSaltNPass(self):
		password = input('Set encryption key: ')
		self.__password = password
		salt = b'x\x86\xe1\xa8^i61\xaa\xe0:b\xb5\xde\xd9\xa3'
		self.__salt = salt

	def __getFiles(self, folder, files):
	    list = os.scandir(folder)
	    for f in list:
	        if f.is_dir() and self.__recur:
	            files = self.__getFiles(f.path, files)
	        if f.is_file():
	            files.append(f.path)
	    return files

	def doStuff(self):
	    fileList = []
	    files = self.__getFiles(self.__folder, fileList)
	    for file in files:
	        if self.__action == 'e':
	            self.__encryptObj.doEncryption(file)
	            print('Encrypted: ' + file)
	        elif self.__action == 'd':
	            self.__encryptObj.doDecryption(file)
	            print('Decrypted: ' + file)

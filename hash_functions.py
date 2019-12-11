# This file contains the functions for generating hashes
import hashlib

def md5hash(text):
	"""Takes in text and returns the md5 hash"""
	hash = hashlib.md5()
	hash.update(text.encode("utf-8"))
	return hash.hexdigest()

def sha1hash(text):
	"""Takes in text and returns the sha1 hash"""
	hash = hashlib.sha1()
	hash.update(text.encode("utf-8"))
	return hash.hexdigest()

def sha224hash(text):
	"""Takes in text and returns the sha224 hash"""
	hash = hashlib.sha224()
	hash.update(text.encode("utf-8"))
	return hash.hexdigest()

def sha256hash(text):
	"""Takes in text and returns the sha256 hash"""
	hash = hashlib.sha256()
	hash.update(text.encode("utf-8"))
	return hash.hexdigest()

def sha384hash(text):
	"""Take in text and returns the sha384 hash"""
	hash = hashlib.sha384()
	hash.update(text.encode("utf-8"))
	return hash.hexdigest()

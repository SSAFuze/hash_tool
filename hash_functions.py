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

def md5crack(hash, list):
	"""Takes in an md5 hash and the path to a wordlist and attempts to crack the hash"""
	cleartext = ''
	with open(list, 'r') as wordlist:
		for line in wordlist:
			if md5hash(line.strip('\n')) == hash:
				cleartext = line
				break
	if cleartext:
		return 'The hash is: '+cleartext
	else:
		return 'Using the provided wordlist, no matches were found'

def sha1crack(hash, list):
        """Takes in an sha1 hash and the path to a wordlist and attempts to crack the hash"""
        cleartext = ''
        with open(list, 'r') as wordlist:
                for line in wordlist:
                        if sha1hash(line.strip('\n')) == hash:
                                cleartext = line
                                break
        if cleartext:
                return 'The hash is: '+cleartext
        else:
                return 'Using the provided wordlist, no matches were found'

def sha224crack(hash, list):
        """Takes in an sha224 hash and the path to a wordlist and attempts to crack the hash"""
        cleartext = ''
        with open(list, 'r') as wordlist:
                for line in wordlist:
                        if sha224hash(line.strip('\n')) == hash:
                                cleartext = line
                                break
        if cleartext:
                return 'The hash is: '+cleartext
        else:
                return 'Using the provided wordlist, no matches were found'

def sha256crack(hash, list):
        """Takes in an sha256 hash and the path to a wordlist and attempts to crack the hash"""
        cleartext = ''
        with open(list, 'r') as wordlist:
                for line in wordlist:
                        if sha256hash(line.strip('\n')) == hash:
                                cleartext = line
                                break
        if cleartext:
                return 'The hash is: '+cleartext
        else:
                return 'Using the provided wordlist, no matches were found'

def sha384crack(hash, list):
        """Takes in an sha384 hash and the path to a wordlist and attempts to crack the hash"""
        cleartext = ''
        with open(list, 'r') as wordlist:
                for line in wordlist:
                        if sha384hash(line.strip('\n')) == hash:
                                cleartext = line
                                break
        if cleartext:
                return 'The hash is: '+cleartext
        else:
                return 'Using the provided wordlist, no matches were found'


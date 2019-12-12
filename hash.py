# This is the python file that should be run to run the program
import hash_functions

welcome_message = "###########################\n\nWelcome to SSAFuze's hash tool! Please see the options below to get you started"
supported_hashes = ['md5', 'sha1', 'sha224', 'sha256', 'sha384']

print(welcome_message)

while True:
	choice = str(input('Please enter 1 to enter the hashing menu, 2 to enter the cracking menu, or type \'exit\' to quit the program: '))
	if choice == '1':
		session_end = False
		while session_end == False:
			hash_type = str(input('Please enter which hash algorithm you wish to use. If you are unsure about what this program supports, enter \'supported\'. If you wish to return to the main menu, enter \'return\': '))
			if hash_type == 'supported':
				print('We support: ')
				for i in supported_hashes:
					print(i)
			
			elif hash_type == 'return':
				session_end = True
			
			elif hash_type in supported_hashes:
				text = str(input('Please enter the text you wish to be hashed: '))
				function = 'hash_functions.' + hash_type + 'hash'
				print(str(eval(function)(text)))

			else:
				print('That is not recognised. Please try again')


	elif choice == '2':
		session_end = False
		while session_end == False:
			crack_type = str(input('Please enter which hash algorithm you wish to crack. If you are unsure about what this program supports, enter \'supported\'. To return to the main menu, enter \'return\': ')) 
			if crack_type == 'supported':
				print('We support: ')
				for i in supported_hashes:
					print(i)

			elif crack_type == 'return':
				session_end = True

			elif crack_type in supported_hashes:
				hash = str(input('Please enter the hash you wish to crack: '))
				path = str(input('Please enter the path to the wordlist you wish to use: '))
				function = 'hash_functions.' + crack_type + 'crack'
				print(str(eval(function)(hash, path)))

			else:
				print('That is not recognised')


	elif choice == 'exit':
		break

	else:
		print('That is not a recognise command, please try again')		

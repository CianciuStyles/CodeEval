import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		components = test.strip().split(' | ')
		word_length = int(components[0])
		last_char = components[1]
		ciphertext = [int(code) for code in components[2].split(' ')]

		found, N, new_ciphertext = False, 0, ''
		while found is False:
			new_ciphertext = ''.join([chr(code-N) for code in ciphertext])
			words = new_ciphertext.split(' ')			
			words_with_right_length = [word for word in words if len(word) == word_length]
			for word in words_with_right_length:
				if word.endswith(last_char) and words_with_right_length.count(word) == 2:
					found = True

			N += 1
		
		print(new_ciphertext)

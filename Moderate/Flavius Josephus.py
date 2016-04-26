import sys

with open(sys.argv[1], 'r') as test_cases:

	for test in test_cases:
		if test == '':
			continue

		N, index = [int(num) for num in test.strip().split(',')]
		arr = list(range(N))

		new_arr, new_index = [], index-1
		while len(arr) > 0:
			elem = arr[new_index]
			new_arr.append(str(elem))
			arr.remove(elem)
			try:
				new_index = (new_index + index - 1) % len(arr)
			except ZeroDivisionError:
				new_index = 0

		print(' '.join(new_arr))
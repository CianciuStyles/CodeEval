import sys

with open(sys.argv[1], 'r') as test_cases:
	board = [[0] * 256 for _ in range(256)]

	for test in test_cases:
		if test == '':
			continue

		command = test.strip().split(' ')
		if command[0] == "SetRow":
			row, value = int(command[1]), int(command[2])
			for col in range(256):
				board[row][col] = value
		elif command[0] == "SetCol":
			col, value = int(command[1]), int(command[2])
			for row in range(256):
				board[row][col] = value
		elif command[0] == "QueryRow":
			row, total = int(command[1]), 0
			for col in range(256):
				total += board[row][col]
			print(total)
		elif command[0] == "QueryCol":
			col, total = int(command[1]), 0
			for row in range(256):
				total += board[row][col]
			print(total)
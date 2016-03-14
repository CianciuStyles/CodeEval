import sys

def main():
	with open(sys.argv[1], 'r') as test_cases:
		for test in test_cases:
			contents = test.split(" ")
			X, Y, N = int(contents[0]), int(contents[1]), int(contents[2])

			result = []
			for num in range(1, N+1):
				current_num = ""
				if num % X == 0 or num % Y == 0:
					if num % X == 0:
						current_num += "F"
					if num % Y == 0:
						current_num += "B"
				else:
					current_num += str(num)

				result.append(current_num)

			print(" ".join(result))


if __name__ == '__main__':
	main()
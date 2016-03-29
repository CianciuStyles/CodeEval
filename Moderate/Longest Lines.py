import heapq
import sys

with open(sys.argv[1], 'r') as test_cases:
	max_heap = []

	for index, test in enumerate(test_cases):
		if test == "":
			continue

		if index == 0:
			N = int(test.strip())

		heapq.heappush(max_heap, test.strip())

	max_list = heapq.nlargest(N, max_heap, key=len)
	for item in max_list:
		print(item)
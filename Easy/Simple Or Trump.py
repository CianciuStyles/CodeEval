import sys

order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
trump_order = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		if test == '':
			continue

		cards, trump = test.strip().split(' | ')
		card_1, card_2 = cards.split(' ')

		rank_1, suit_1 = order.index(card_1[:-1]), card_1[-1]
		rank_2, suit_2 = order.index(card_2[:-1]), card_2[-1]

		if suit_1 != trump and suit_2 != trump:
			if rank_1 == rank_2:
				print(card_1 + ' ' + card_2)
			else:
				print(card_1 if rank_1 > rank_2 else card_2)
		else:
			if suit_1 == trump:
				if suit_2 == trump:
					rank_1 = trump_order.index(card_1[:-1])
					rank_2 = trump_order.index(card_2[:-1])
					
					if rank_1 == rank_2:
						print(card_1 + ' ' + card_2)
					else:
						print(card_1 if rank_1 > rank_2 else card_2)
				else:
					print(card_1)
			else:
				print(card_2)
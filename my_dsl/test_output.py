def count_bombs_around(bombs, x, y):
	count = 0
	for i in range(max(0, x - 1), min(len(bombs), x + 2)):
		for j in range(max(0, y - 1), min(len(bombs[0]), y + 2)):
			if bombs[i][j]:
				count += 1
	return count

def print_board_with_hint(bombs, hint=False):
	for i in range(len(bombs)):
		for j in range(len(bombs[0])):
			if hint and not bombs[i][j]:
				bombs_around = count_bombs_around(bombs, i, j)
				if bombs_around == 0:
					bombs_around = '#'
				print(bombs_around, end='')
			elif not bombs[i][j]:
				print('#', end='')
			else:
				print('*', end='')
		print()
bombs = [[False for y in range(80)] for x in range(5)]
bombs[0][1] = True
bombs[3][5] = True
bombs[4][7] = True
print_board_with_hint(bombs, hint=True)
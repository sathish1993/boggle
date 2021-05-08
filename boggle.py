from queue import Queue

def find_match_char(i, j, r_len, c_len, word_index, word, boggle_grid):
	for i in range(r_len):
		for j in range(c_len):	
			if boggle_grid[i][j] == word[word_index]:
				return [i, j]
	return [-1, -1]

def is_word_available_helper(temp_index, r_len, c_len, word_index, word, temp_grid):
	q = Queue()
	word_len = len(word)

	print(temp_index)
	i = temp_index[0]
	j = temp_index[1]
	if i == -1 and j == -1:
		return bool(False), i, j		
		
	q.put([i,j])
	temp_grid[i][j] = '_'	
	word_index += 1;

	a = 1

	while not q.empty():
		print('inside while word_index ', word_index, ' word_len', word_len)
		temp = q.get()
		r = temp[0]
		c = temp[1]

		if a == 1 and(r+1)<r_len and word_index<word_len and temp_grid[r+1][c] == word[word_index]: #down
			#word_index += 1
			#print(word_index[r+1][c])
			print("down")
			q.put([r+1,c])
			temp_grid[r+1][c] = '_'
			a = 0

		if a == 1 and (r-1)>=0 and word_index<word_len and temp_grid[r-1][c] == word[word_index]: #up
			#word_index += 1
			#print(word_index[r+1][c])
			print("up")
			q.put([r-1,c])
			temp_grid[r-1][c] = '_'
			a = 0

		if a == 1 and (c+1)<c_len and word_index<word_len and temp_grid[r][c+1] == word[word_index]: #right
			#word_index += 1
			print("right")
			q.put([r,c+1])
			temp_grid[r][c+1] = '_'
			a = 0

		if a == 1 and (c-1)>=0 and word_index<word_len and temp_grid[r][c-1] == word[word_index]: #left
			#word_index += 1
			print("left")
			q.put([r,c-1])
			temp_grid[r][c-1] = '_'
			a = 0

		if a == 1 and (r-1)>=0 and (c-1)>=0 and word_index<word_len and temp_grid[r-1][c-1] == word[word_index]: #topleft
			#word_index += 1
			print("topleft")
			q.put([r-1,c-1])
			temp_grid[r-1][c-1] = '_'		
			a = 0				

		if a == 1 and (r-1)>=0 and (c+1)<c_len and word_index<word_len and temp_grid[r-1][c+1] == word[word_index]: #topright
			#word_index +=1
			print("topright")
			q.put([r-1,c+1])
			temp_grid[r-1][c+1] = '_'
			a = 0
		
		if a == 1 and (r+1)<r_len and (c-1)>=0 and word_index<word_len and temp_grid[r+1][c-1] == word[word_index]: #bottomleft
			#word_index +=1
			print("bottomleft")
			q.put([r+1,c-1])
			temp_grid[r+1][c-1] = '_'
			a = 0

		if a == 1 and (r+1)<r_len and (c+1)<c_len and word_index<word_len and temp_grid[r+1][c+1] == word[word_index]: #bottomright
			#word_index +=1
			print("bottomright")
			q.put([r+1,c+1])
			temp_grid[r+1][c+1] = '_'
			a = 0

		if a == 0:
			a = 1
			print("should inc word_index?? ", word[word_index], "~~~~ qsize", q.qsize())
			word_index += 1
			print("word_index is ", word_index)
		#elif a == 1:
		#	print("hey no-->", word[word_index], "~~~~ qsize", q.qsize())

		i = r
		j = c


	print('outside while word_index ', word_index, ' word_len', word_len)
	#print("prefinal check~~~~word_len", word_len, "~~word[word_index]", word[word_index], "~~~~ qsize", q.empty())
	if word_len == word_index:
		#print("final check~~~~word_len", word_len, "~~word[word_index]", word[word_index], "~~~~ qsize", q.empty())
		return bool(True), r, c
	#print("postfinal check~~~~word_len", word_len, "~~word[word_index]", word[word_index], "~~~~ qsize", q.empty())

	return bool(False), i, j
	


def is_word_available(boggle_grid, word):
	if word == None or len(word) < 1:
		return bool(false)

	r_len = len(boggle_grid)
	if r_len < 1:
		return bool(false)

	c_len = len(boggle_grid[0])	


	temp_grid = boggle_grid

	#print(r_len , "~~~", c_len)	
	 
	temp_index = find_match_char(0, 0, r_len, c_len, 0, word, temp_grid)	
	#print(temp_index , "++++")
	ret_val, i, j = is_word_available_helper(temp_index, r_len, c_len, 0, word, temp_grid)


	if ret_val:
		return bool(True)

	print('end round 1-->', ret_val)
	print(i, "~~~~", j, "~~~~", word[0], "~~~", r_len, "~~~", c_len)

	count = 0
	while i < r_len and j < c_len:
		temp_grid = boggle_grid
		temp_index = find_match_char(i, j, r_len, c_len, 0, word, temp_grid)

		if temp_index[0] == -1 and temp_index[1] == -1:
			return bool(False)

		print("temp_index line 134-> ", temp_index)
		ret_val, i, j = is_word_available_helper(temp_index, r_len, c_len, 0, word, temp_grid)

		print(i, "~~~~", j, "~~~~", r_len, "~~~", c_len, "~~~", ret_val)
		if ret_val:
			return bool(True)


	return bool(False)						



def main(): 
	boggle_grid = [ ['H','N','S','E'], ['A','R','G','U'], ['B','R','U','S'], ['F','E','T','I'] ]	
	word = 'HNSEUSITEFBARGUR'

	print(is_word_available(boggle_grid, word))

	# for i in range(0, len(boggle_grid)):
	# 	print boggle_grid[i]


if __name__ == '__main__':
	main()
from queue import Queue

class Boggle(object):

	"""docstring for Boggle"""
	def __init__(self):
		super(Boggle, self).__init__()
		self.my_queue = None
		self.direction_check = 1

	# Method to find the starting char of given input string
	def find_match_char(self, i, j, r_len, c_len, word_index, word, temp_grid):
		for i in range(r_len):
			for j in range(c_len):	
				if temp_grid[i][j] == word[word_index]:
					return [i, j]
		return [-1, -1]


	# Helper method to check if given input string is part of boggle
	def is_word_available_helper(self, temp_index, r_len, c_len, word_index, word, temp_grid):	
		word_len = len(word)

		i = temp_index[0]
		j = temp_index[1]

		if i == -1 and j == -1:
			return bool(False), i, j		

		self.my_queue.put([i,j])
		temp_grid[i][j] = '_'	
		word_index += 1;

		self.direction_check = 1
		while not self.my_queue.empty():		
			temp = self.my_queue.get()
			r = temp[0]
			c = temp[1]

			if self.direction_check == 1 and(r+1)<r_len and word_index<word_len and temp_grid[r+1][c] == word[word_index]: #down				
				self.my_queue.put([r+1,c])
				temp_grid[r+1][c] = '_'
				self.direction_check = 0
			if self.direction_check == 1 and (r-1)>=0 and word_index<word_len and temp_grid[r-1][c] == word[word_index]: #up				
				self.my_queue.put([r-1,c])
				temp_grid[r-1][c] = '_'
				self.direction_check = 0
			if self.direction_check == 1 and (c+1)<c_len and word_index<word_len and temp_grid[r][c+1] == word[word_index]: #right				
				self.my_queue.put([r,c+1])
				temp_grid[r][c+1] = '_'
				self.direction_check = 0
			if self.direction_check == 1 and (c-1)>=0 and word_index<word_len and temp_grid[r][c-1] == word[word_index]: #left
				self.my_queue.put([r,c-1])
				temp_grid[r][c-1] = '_'
				self.direction_check = 0
			if self.direction_check == 1 and (r-1)>=0 and (c-1)>=0 and word_index<word_len and temp_grid[r-1][c-1] == word[word_index]: #topleft
				self.my_queue.put([r-1,c-1])
				temp_grid[r-1][c-1] = '_'		
				self.direction_check = 0				
			if self.direction_check == 1 and (r-1)>=0 and (c+1)<c_len and word_index<word_len and temp_grid[r-1][c+1] == word[word_index]: #topright
				self.my_queue.put([r-1,c+1])
				temp_grid[r-1][c+1] = '_'
				self.direction_check = 0
			if self.direction_check == 1 and (r+1)<r_len and (c-1)>=0 and word_index<word_len and temp_grid[r+1][c-1] == word[word_index]: #bottomleft
				self.my_queue.put([r+1,c-1])
				temp_grid[r+1][c-1] = '_'
				self.direction_check = 0
			if self.direction_check == 1 and (r+1)<r_len and (c+1)<c_len and word_index<word_len and temp_grid[r+1][c+1] == word[word_index]: #bottomright
				self.my_queue.put([r+1,c+1])
				temp_grid[r+1][c+1] = '_'
				self.direction_check = 0
			if self.direction_check == 0:
				self.direction_check = 1			
				word_index += 1					

			i = r
			j = c

		if word_len == word_index:
			return bool(True), r, c

		return bool(False), i, j



	# Method to check if given input string is part of boggle
	def is_word_available(self, word, boggle_grid):		
		if word == None or len(word) < 1:
			return bool(False)

		r_len = len(boggle_grid)
		if r_len < 1:
			return bool(False)

		self.my_queue = Queue()
		c_len = len(boggle_grid[0])
		temp_index = self.find_match_char(0, 0, r_len, c_len, 0, word, boggle_grid)			
		ret_val, i, j = self.is_word_available_helper(temp_index, r_len, c_len, 0, word, boggle_grid)
		if ret_val:
			return bool(True)

		while i < r_len and j < c_len:			
			temp_index = self.find_match_char(i, j, r_len, c_len, 0, word, boggle_grid)
			if temp_index[0] == -1 and temp_index[1] == -1:
				return bool(False)

			ret_val, i, j = self.is_word_available_helper(temp_index, r_len, c_len, 0, word, boggle_grid)
			if ret_val:
				return bool(True)

		return bool(False)	
		
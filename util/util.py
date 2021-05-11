import sys
import itertools

class Util(object):
	"""docstring for Util"""
	def __init__(self):		
		self.combo_list = set()
		self.permutated_list = []

	def get_words(self):		
		dict_path = None
		eng_words = []
		if sys.platform == 'linux' or sys.platform == "linux2":
			dict_path = '/usr/dict/words'
		elif sys.platform == 'darwin':
			dict_path = '/usr/share/dict/words'

		in_file = open(dict_path, 'r')
		for line in in_file.readlines():					
			eng_words.append(line.strip().upper())		
		
		return eng_words


	def find_all_combinations_helper(self, final_grid_str, combo_word, start_index):

		for i in range(start_index, len(final_grid_str)):
			combo_word += final_grid_str[i]
			if combo_word not in self.combo_list:
				self.combo_list.add(combo_word)
			self.find_all_combinations_helper(final_grid_str, combo_word, i+1)
			combo_word = combo_word[:-1]


	def find_permutations_of_all_words_helper(self, in_str, left, right):
		if left == right:
			my_str = ''.join(in_str)
			if my_str not in self.permutated_list:
				self.permutated_list.append(my_str)
		else:
			for i in xrange(left, right + 1):
				in_str[left], in_str[i] = in_str[i], in_str[left]
				self.find_permutations_of_all_words_helper(in_str, left+1, right)
				in_str[left], in_str[i] = in_str[i], in_str[left]


	def find_permutations_of_all_words(self):
		perm_list = []
		for word in self.combo_list:
			print(word)
			#in_str = list(word)			
			#self.find_permutations_of_all_words_helper(in_str, 0, len(word)-1)

			perms = [''.join(p) for p in permutations(word)]
			perm_list.extend(set(perms))

		return perm_list


	def find_all_combinations(self, boggle_grid):		 
		concat_list = []	
		combinations = []

		for line in boggle_grid:
			concat_list += line
		final_grid_str = ''.join(concat_list)

		for i in range(len(final_grid_str)):
			combinations.extend([''.join(x) for x in itertools.permutations(final_grid_str, i + 1)])


		combinations = set(combinations)
		print(combinations)
		#self.find_all_combinations_helper(final_grid_str, '', 0)
		#print(self.combo_list)
		#perm_list = self.find_permutations_of_all_words()

		
		#print("*****************************************\n\n\n\n")
		#print(perm_list)
		return combinations
		
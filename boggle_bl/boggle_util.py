import os, sys

class BoggleUti(object):

	"""docstring for BoggleUti"""
	def __init__(self, file_path):
		super(BoggleUti, self).__init__()
		self.input_file_path = file_path
		self.boggle_grid = []

	# Util method to check if given path exists
	def check_if_path_exists(self, in_path):
		if not os.path.exists(in_path):
			print('{} does not exist.'.format(in_path))
			return bool(False)
		return bool(True)
	
	# Util method to read input file
	def read_input_file(self):
		if not self.check_if_path_exists(self.input_file_path):
			sys.exit(-1)

		in_file = open(self.input_file_path, 'r')
		for line in in_file.readlines():	
			self.boggle_grid.append(line.split())
		return self.boggle_grid

	# Util method to read dict from /usr/share/dict/words on a mac, and /usr/dict/words on linux
	def get_english_dict_words(self):
		dict_path = None
		eng_words = []

		if sys.platform == 'linux' or sys.platform == "linux2":
			dict_path = '/usr/dict/words'
		elif sys.platform == 'darwin':
			dict_path = '/usr/share/dict/words'

		if not self.check_if_path_exists(dict_path):
			sys.exit(-1)

		in_file = open(dict_path, 'r')
		for line in in_file.readlines():					
			eng_words.append(line.strip())		
		return eng_words

	#Util method to print findings in a txt file
	def gen_valid_boggle_words(self, valid_boggle_findings):
		out_file = open('valid_boggle_findings.txt', 'w')
		for word in valid_boggle_findings:
			out_file.write(word + '\n')
		out_file.close()

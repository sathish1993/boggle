class Dictionary(object):
	"""docstring for Dictionary"""
	def __init__(self, eng_words):
		self.eng_words = eng_words

	def is_word(self, input_str):
		return input_str in self.eng_words
		
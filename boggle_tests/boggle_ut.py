import unittest
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from boggle_bl import boggle, boggle_util


'''
	Unit test file to check if the writtern methods work as expected.
'''

class BoggleTest(unittest.TestCase):

	# Example words from README
	# Test : 1
	def test_find_if_word_in_boggle_positive1(self):
		word = 'TRUE'
		word_grid = [['H', 'N', 'S', 'E'], ['A', 'R', 'G', 'U'], ['B', 'R', 'U', 'S'], ['F', 'E', 'T', 'I']]

		return_value = boggle.Boggle().is_word_available(word, word_grid)		
		self.assertEqual(return_value, True)

	# Test : 2
	def test_find_if_word_in_boggle_positive2(self):
		word = 'USGRA'
		word_grid = [['H', 'N', 'S', 'E'], ['A', 'R', 'G', 'U'], ['B', 'R', 'U', 'S'], ['F', 'E', 'T', 'I']]

		return_value = boggle.Boggle().is_word_available(word, word_grid)		
		self.assertEqual(return_value, True)

	# Test : 3
	def test_find_if_word_in_boggle_positive3(self):
		word = 'SUGRA'
		word_grid = [['H', 'N', 'S', 'E'], ['A', 'R', 'G', 'U'], ['B', 'R', 'U', 'S'], ['F', 'E', 'T', 'I']]

		return_value = boggle.Boggle().is_word_available(word, word_grid)		
		self.assertEqual(return_value, True)

	# Test : 4
	def test_find_if_word_in_boggle_negative1(self):
		word = 'SUGAR'
		word_grid = [['H', 'N', 'S', 'E'], ['A', 'R', 'G', 'U'], ['B', 'R', 'U', 'S'], ['F', 'E', 'T', 'I']]

		return_value = boggle.Boggle().is_word_available(word, word_grid)		
		self.assertEqual(return_value, False)

	# Test : 5
	def test_find_if_word_in_boggle_negative2(self):
		word = 'SIS'
		word_grid = [['H', 'N', 'S', 'E'], ['A', 'R', 'G', 'U'], ['B', 'R', 'U', 'S'], ['F', 'E', 'T', 'I']]

		return_value = boggle.Boggle().is_word_available(word, word_grid)		
		self.assertEqual(return_value, False)

	# Test : 6
	def test_find_if_word_in_boggle_negative3(self):
		word = 'BRUSH'
		word_grid = [['H', 'N', 'S', 'E'], ['A', 'R', 'G', 'U'], ['B', 'R', 'U', 'S'], ['F', 'E', 'T', 'I']]

		return_value = boggle.Boggle().is_word_available(word, word_grid)		
		self.assertEqual(return_value, False)

	# Test : 7
	def test_find_if_word_in_boggle_input_word_empty(self):
		word = ''
		word_grid = [['H', 'N', 'S', 'E'], ['A', 'R', 'G', 'U'], ['B', 'R', 'U', 'S'], ['F', 'E', 'T', 'I']]

		return_value = boggle.Boggle().is_word_available(word, word_grid)		
		self.assertEqual(return_value, False)

	# Test : 8
	def test_find_if_word_in_boggle_input_word_none(self):
		word = None
		word_grid = [['H', 'N', 'S', 'E'], ['A', 'R', 'G', 'U'], ['B', 'R', 'U', 'S'], ['F', 'E', 'T', 'I']]

		return_value = boggle.Boggle().is_word_available(word, word_grid)		
		self.assertEqual(return_value, False)

	# Test : 9
	def test_find_if_word_in_boggle_input_word_grid_3x4(self):
		word = 'TUG'
		word_grid = [['H', 'N', 'S'], ['A', 'R', 'G'], ['B', 'R', 'U'], ['F', 'E', 'T']]

		return_value = boggle.Boggle().is_word_available(word, word_grid)		
		self.assertEqual(return_value, True)

	# Test : 10
	def test_find_if_word_in_boggle_input_word_grid_none(self):
		word = 'TUG'
		word_grid = [[],[],[]]

		return_value = boggle.Boggle().is_word_available(word, word_grid)		
		self.assertEqual(return_value, False)


	# other worthwhile tests:
	# 1. performance/scalability tests  for 10K, 100K, 1M words
	# 2. multiprocessing/threading tests
	# 3. test util methods if paths exists, if write-output-to-file works


if __name__ == '__main__':
    unittest.main()
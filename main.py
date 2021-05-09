from boggle_bl import boggle
from boggle_bl import boggle_util

import sys
import time
import datetime
import copy

# Method to initiate boggle
def init_boggle_game(boggle_obj, eng_words, boggle_grid):
	valid_words = []
	start_time  = round(time.time() * 1000)	
	for word in eng_words:						
		word = word.upper()
		temp_grid = copy.deepcopy(boggle_grid)			
		if boggle_obj.is_word_available(word, temp_grid) and word not in valid_words:
			valid_words.append(word)
			
	end_time = round(time.time() * 1000)
	valid_words = sorted(valid_words)
	print('Total number of findings {}'.format(len(valid_words)))
	print('Total time taken {}s'.format((end_time - start_time) / 1000.0))
	return valid_words

def main():

	if len(sys.argv) != 2:
		print('Please execute the code like python main.py /Users/sathish/Desktop/boggle/input_grid.txt')
		sys.exit(-1)	

	boggle_util_obj = boggle_util.BoggleUti(sys.argv[1])	
	boggle_grid = boggle_util_obj.read_input_file()
	eng_words = boggle_util_obj.get_english_dict_words()		
	boggle_obj = boggle.Boggle()

	valid_words = init_boggle_game(boggle_obj, eng_words, boggle_grid)
	
	boggle_util_obj.gen_valid_boggle_words(valid_words)


if __name__ == '__main__':
	main()
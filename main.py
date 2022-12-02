from boggle_bl import boggle
from boggle_bl import boggle_util

from eng_dictionary import dictionary
from util import util

import sys
import time
import datetime
import copy

# Method to initiate boggle1
def get_all_words(boggle_obj, boggle_grid, dict_obj, combo_list):
	valid_words = []	
	count = 0
	for word in combo_list:	
		print(word, "~~", count)
		count += 1
		if dict_obj.is_word(word):				
			print("AVAILABLE")
			temp_grid = copy.deepcopy(boggle_grid)			
			if boggle_obj.is_word_available(word, temp_grid) and word not in valid_words:
				valid_words.append(word)	
	return valid_words

def main():

	if len(sys.argv) != 2:
		print('Please execute the code like python main.py /Users/sathish/Desktop/boggle/input_grid.txt')
		sys.exit(-1)	

	boggle_util_obj = boggle_util.BoggleUti(sys.argv[1])	
	boggle_grid = boggle_util_obj.read_input_file()
	boggle_obj = boggle.Boggle()

	util_obj = util.Util()	
	dict_obj = dictionary.Dictionary(set(util_obj.get_words()))

	start_time  = round(time.time() * 1000)	

	combo_list = util_obj.find_all_combinations(boggle_grid)
	print(len(combo_list))
	valid_words = get_all_words(boggle_obj, boggle_grid, dict_obj, combo_list)
	
	end_time = round(time.time() * 1000)
	
	valid_words = sorted(valid_words)

	print('Total number of findings {}'.format(len(valid_words)))
	print('Total time taken {}s'.format((end_time - start_time) / 1000.0))
	boggle_util_obj.gen_valid_boggle_words(valid_words)


if __name__ == '__main__':
	main()

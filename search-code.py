import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
import operator

def sort_alph(some_dict):
	### Sort alphabetically
	some_list = some_dict.items()
	sorted_alph = sorted(some_list)
	alph_x, alph_y = zip(*sorted_alph)
	return alph_x, alph_y

def sort_val(some_dict):
	### Sort numerically
	sorted_val = sorted(some_dict.items(), key=operator.itemgetter(1), reverse = True)
	val_x, val_y = zip(*sorted_val)
	return val_x, val_y

def search_letters(in_words, letter, operation):
	### gets words that have/don't have certain letters
	out_words = []
	if operation == "add":
		for word in in_words:
			if word.count(letter) > 0:
				out_words.append(word)
	elif operation == "sub":
		for word in in_words:
			if word.count(letter) == 0:
				out_words.append(word)
	else:
		print("invalid operation type")
		pass
	return out_words

def plot_word_frequency(in_words, num, in_string):
	### get letter frequencies and plot them
	## Concatinate words into one string
	letters = ''
	for word in in_words:
		letters += word
	## Get frequency of letters
	letters_dict = Counter(letters)
	## Sort and separate letters and values
	# letter_alph, value_alph = sort_alph(letters_dict)
	# perc_alph = np.around(np.array(value_alph)/num*100,0)
	letter_val, value_val = sort_val(letters_dict)
	perc_val = np.around(np.array(value_val)/num*100,0)
	## Plot frequency of letters
	## Alphabetically
	# plt.bar(letter_alph, perc_alph)
	# plt.title("Frequency of letters in possible Wordle answers\nAlphabetically sorted")
	# #plt.savefig("/home/tess/Documents/Wordle/Wordle-main/letter_freq_"+in_string+"_alph.png")
	# plt.ylabel("Percentage (%)")
	# plt.xlabel("Letters")
	# plt.show()
	# plt.clf()
	## Numerically
	plt.bar(letter_val, perc_val)
	plt.title("Frequency of letters in possible Wordle answers\nNumerically sorted")
	#plt.savefig("/home/tess/Documents/Wordle/Wordle-main/letter_freq_"+in_string+"_val.png")
	plt.ylabel("Percentage of words containing each letter (%)")
	plt.xlabel("Letters")
	plt.show()
	plt.clf()

def pop_known(in_words, in_letters):
	### remove known letters for frequency stats
	letters = ''
	for word in in_words:
		letters += word
	out_letters = "".join(c for c in letters if c.lower() not in in_letters)
	return out_letters

def get_good_locations(locations, in_words):
	# deal with known correct letter locations
	loc_num = 0
	temp_words = []
	for loc in locations:
		if loc != '':
			for word in in_words:
				# search for letter in location index loc_num
				if word[loc_num] == loc:
					temp_words.append(word)
		loc_num += 1
	return temp_words

def get_bad_locations(locations, in_words):
	# deal with known incorrect letter locations
	loc_num = 0
	for loc in locations:
		if loc != '':
			for elem in loc: # to deal with multiple letters
				for word in in_words:
					# search for letter in location index loc_num
					if word[loc_num] == elem:
						in_words.remove(word)
		loc_num += 1
	return in_words

### Read words from file
with open("/home/tess/Documents/Wordle/Wordle-main/eligible-words.txt", "r") as f:
	words = f.read().splitlines()

# plot_word_frequency(words, len(words), "+00")

### After some guesses

#################### USER INPUT ####################
# known letters both included or not included
include_letters = "eu"
eliminate_letters = "adi"
good_locations = ['','','','e','']
bad_locations = ['','','','','u']
####################################################

# get words that include known letters
new_words = words
if include_letters != "":
	for letter in include_letters:
		new_words = search_letters(new_words, letter, "add")

# get words that do not include known letters
if eliminate_letters != "":
	for not_letter in eliminate_letters:
		new_words = search_letters(new_words, not_letter, "sub")

# remove known letters from stats
unknown_letters = pop_known(new_words, include_letters)

# plot stats
# plot_word_frequency(unknown_letters, len(new_words), "+"+include_letters+"-"+eliminate_letters)

new_words = get_good_locations(good_locations, new_words)
new_words = get_bad_locations(bad_locations, new_words)

# print to user
print("Possible words: ")
print(new_words)

# plot_word_frequency(new_words, len(new_words), "locations")

### TO DO: Plot expectation values and sort remaining possible words based on that

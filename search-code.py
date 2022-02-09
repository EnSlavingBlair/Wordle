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

def plot_word_frequency(in_words, in_string):
	### get letter frequencies and plot them
	# Concatinate words into one string
	letters = ''
	for word in in_words:
		letters += word
	# Get frequency of letters
	letters_dict = Counter(letters)
	# Sort and separate letters and values
	letter_alph, value_alph = sort_alph(letters_dict)
	letter_val, value_val = sort_val(letters_dict)
	# Plot frequency of letters
	# Alphabetically
	plt.bar(letter_alph, value_alph)
	plt.title("Frequency of letters in possible Wordle answers\nAlphabetically sorted")
	plt.savefig("/home/tess/Documents/Wordle/letter_freq_"+in_string+"_alph.png")
	plt.clf()
	# Numerically
	plt.bar(letter_val, value_val)
	plt.title("Frequency of letters in possible Wordle answers\nNumerically sorted")
	plt.savefig("/home/tess/Documents/Wordle/letter_freq_"+in_string+"_val.png")
	plt.clf()

def pop_known(in_words, in_letters):
	### remove known letters for frequency stats
	letters = ''
	for word in in_words:
		letters += word
	out_letters = "".join(c for c in letters if c.lower() not in in_letters)
	return out_letters

### Read words from file
with open("/home/tess/Documents/Wordle/eligible-words.txt", "r") as f:
	words = f.read().splitlines()

plot_word_frequency(words, "+00")

### After some guesses

# known letters both included or not included
include_letters = "uor"
eliminate_letters = "adiesnt"

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
plot_word_frequency(unknown_letters, "+"+include_letters+"-"+eliminate_letters)

# print to user
print("Possible words: ")
print(new_words)

### TO DO: Add functionality that takes into account known position of letters




import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
import operator

def sort_alph(some_dict):
	# Sort alphabetically
	some_list = some_dict.items()
	sorted_alph = sorted(some_list)
	alph_x, alph_y = zip(*sorted_alph)
	return alph_x, alph_y

def sort_val(some_dict):
	# Sort numerically
	sorted_val = sorted(some_dict.items(), key=operator.itemgetter(1), reverse = True)
	val_x, val_y = zip(*sorted_val)
	return val_x, val_y

### Read words from file
with open("/home/tess/Documents/Wordle/eligible-words.txt", "r") as f:
	words = f.read().splitlines()

### Contatinate words into one string
letters = ''
for word in words:
	letters += word

### Get frequency of letters
letters_dict = Counter(letters)

### Sort and separate letters and values
letter_alph, value_alph = sort_alph(letters_dict)
letter_val, value_val = sort_val(letters_dict)

### Plot frequency of letters

# Alphabetically
plt.bar(letter_alph, value_alph)
plt.title("Frequency of letters in possible Wordle answers\nAlphabetically sorted")
plt.savefig("/home/tess/Documents/Wordle/letter-freq-alph.png")
plt.clf()

# Numerically
plt.bar(letter_val, value_val)
plt.title("Frequency of letters in possible Wordle answers\nNumerically sorted")
plt.savefig("/home/tess/Documents/Wordle/letter-freq-val.png")
plt.clf()

### TO DO: Make list of letter frequencies given one or many letters are either present o not present



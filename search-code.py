import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
import operator

words = np.zeros(2315)

with open("/home/tess/Documents/Wordle/eligible-words.txt", "r") as f:
	words = f.read().splitlines()

letters = ''
for word in words:
	letters += word

print(words)
print(letters)

letters_dict = Counter(letters)

print(letters_dict)

letters_list = letters_dict.items()

def sort_alph(some_list):
	# Sort alphabetically
	sorted_alph = sorted(some_list)
	alph_x, alph_y = zip(*sorted_alph)
	return alph_x, alph_y

letter_alph, value_alph = sort_alph(letters_list)
plt.bar(letter_alph, value_alph)
plt.title("Frequency of letters in possible Wordle answers\nAlphabetically sorted")
plt.savefig("/home/tess/Documents/Wordle/letter-freq-alph.png")
plt.clf()

def sort_val(some_dict):
	# Sort numerically
	sorted_val = sorted(some_dict.items(), key=operator.itemgetter(1), reverse = True)
	val_x, val_y = zip(*sorted_val)
	return val_x, val_y

letter_val, value_val = sort_val(letters_dict)
plt.bar(letter_val, value_val)
plt.title("Frequency of letters in possible Wordle answers\nNumerically sorted")
plt.savefig("/home/tess/Documents/Wordle/letter-freq-val.png")
plt.clf()

### TO DO: Make list of letter frequencies given one or many letters are either present o not present




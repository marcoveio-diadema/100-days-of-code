import pandas

phonetic = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_letters = {row.letter: row.code for (index, row) in phonetic.iterrows()}


name = input("What's your name?: ").upper()

name_list = [nato_letters[letter] for letter in name]

print(name_list)


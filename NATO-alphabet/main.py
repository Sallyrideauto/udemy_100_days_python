import pandas

nato_code_data = pandas.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
nato_code_dict = {row.letter: row.code for (index, row) in nato_code_data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name_code = [nato_code_dict[letter] for letter in input("Enter a word: ").upper()]
print(name_code)
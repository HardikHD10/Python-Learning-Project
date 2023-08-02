import pandas

flag = True
while(flag):
    try :
        #TODO 1. Create a dictionary in this format:
        data = pandas.read_csv("nato_phonetic_alphabet.csv")
        data_dict = {row.letter : row.code  for (index,row) in data.iterrows()}
        # print(data_dict)

        #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
        user_input = input("Enter the word for NATO Phonetics : ").upper()
        output = {letter : data_dict[letter] for letter in user_input}
        print(output)

    except KeyError:
        print("Sorry, Only letters in alphabet please !")


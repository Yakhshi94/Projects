import pandas

# while True:
#     try:
#         data = pandas.read_csv('nato_phonetic_alphabet.csv')
#         phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
#         user_input = input('Enter Your word: ').upper()
#         phonetic_list = [phonetic_dict[code] for code in user_input]
#
#     except KeyError:
#         print('Sorry, Only letters in the alphabets please.')
#     else:
#         print(phonetic_list)
#         break

data = pandas.read_csv('nato_phonetic_alphabet.csv')
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    user_input = input('Enter Your word: ').upper()
    try:
        phonetic_list = [phonetic_dict[code] for code in user_input]

    except KeyError:
        print('Sorry, Only letters in the alphabets please.')
        generate_phonetic()
    else:
        print(phonetic_list)


generate_phonetic()

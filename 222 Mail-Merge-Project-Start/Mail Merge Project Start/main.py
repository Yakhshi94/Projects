# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('Input/Names/invited_names.txt') as names_file:
    # invited_list = names_file.readlines()
    invited_list = names_file.read()
    names = invited_list.split('\n')

with open('Input/Letters/starting_letter.txt') as invite_letter:
    letter_temp = invite_letter.read()
    for name in names:
        ready_to_send = letter_temp.replace('[name]', name)
        with open(f'Output/ReadyToSend/letter_for_{name}.txt', mode='w') as letter:
            letter.write(ready_to_send)

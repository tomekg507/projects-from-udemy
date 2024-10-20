letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
           'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
morse_code = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..',
              '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.',
              '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', ' ']

def translate(word):
        translated_word = ''
        for letter in word.lower():
            index = letters.index(letter)
            #print(morse_code[index], end=' ')
            translated_word += f'{morse_code[index]} '
        return translated_word



print('String to Morse Translator. \n')
to_continue = True

while to_continue:
    try:
        word_to_translate = input('Type a word: ')
        translated_word = translate(word_to_translate)
    except ValueError:
        print('Please use only letters and spaces')
    else:
        print(translated_word)
        exit = input('\nPress q to exit or any key to continue:')
        if exit == 'q':
            to_continue = False

print('Bye bye!!')
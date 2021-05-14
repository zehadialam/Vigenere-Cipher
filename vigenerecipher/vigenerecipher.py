def the_alphabet():
    """Return a list containing the alphabet as individual characters."""
    return ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def convert_letter_to_number(text):
    """Return a list with the numeric position (starting at zero) in the alphabet for each letter of the inputted
    argument.

    Example: >>> convert_letter_to_number('python')
                 [15, 24, 19, 7, 14, 13]
    """
    try:
        text_no_spaces = text.replace(' ', '')  # removing whitespace
        letter_to_number = [0] * len(text_no_spaces)  # initialize list with zeros
        alphabet = the_alphabet()
        k = 0
        for i in range(0, len(text)):
            for j in range(0, len(alphabet)):
                if text[i] == alphabet[j] or text[i] == alphabet[j].upper():
                    letter_to_number[k] = j  # assigning index of character to list position 'k'
                    k += 1
        return letter_to_number
    except AttributeError:
        print('Invalid input! Must only input alphabetic strings.')


def convert_number_to_letter(letter_to_number):
    """Return a string that is the alphabetic equivalent for a list of numbers.

    Example: >>> convert_number_to_letter([15, 24, 19, 7, 14, 13])
                 python
    """
    try:
        for i in range(0, len(letter_to_number)):
            if not isinstance(letter_to_number[i], int):  # check if every element is int
                raise TypeError
        message_only_alphabetic = ''
        for i in range(0, len(letter_to_number)):
            for j in range(0, len(the_alphabet())):
                if letter_to_number[i] == j:
                    message_only_alphabetic += the_alphabet()[j]  # concatenating alphabetic character
        return message_only_alphabetic
    except TypeError:
        print('Invalid input! Must only input iterables containing data of type int.')


def restore_original_format(original_format, modified_format):
    """Return a string with the format of 'original_format' (i.e. including spaces and punctuation).

    Example: >>> restore_original_format('Ice - Cream', 'abcdefgh')
                 Abc - Defgh
    """
    restored_text = ''
    j = 0
    for i in range(0, len(original_format)):
        if original_format[i].isalpha():
            # accounting for letter casing
            if original_format[i].isupper():
                restored_text += modified_format[j].upper()
            elif original_format[i].islower():
                restored_text += modified_format[j].lower()
            else:
                restored_text += modified_format[j]
            j += 1
        elif original_format[i].isspace():  # accounting for spaces in original_format text
            restored_text += ' '
        else:
            restored_text += original_format[i]  # accounting for other non-alphabetic characters
    return restored_text


def vigenere_cipher(text, key, process):
    """Return the encrypted or decrypted version of inputted text, based on the process and key specified.

    Example: >>> vigenere_cipher('Quantum theory', 'physics', 'encrypt')
                 Fbyfbwe iocgza

             >>> vigenere_cipher('Fbyfbwe iocgza', 'physics', 'decrypt')
                 Quantum theory
    """
    text_copy = text  # make a copy of text to be used for restoring original format later
    letter_to_number = convert_letter_to_number(text)
    vigenere_cipher_shifts = {}  # dictionary for holding shift values
    shift_value = convert_letter_to_number(key)
    for i in range(len(letter_to_number)):
        vigenere_cipher_shifts[i] = shift_value[i % len(key)]
    for i in range(0, len(letter_to_number)):
        if process.lower() == 'encrypt':
            letter_to_number[i] = (letter_to_number[i] + vigenere_cipher_shifts.get(i)) % len(the_alphabet())
        elif process.lower() == 'decrypt':
            letter_to_number[i] = (letter_to_number[i] - vigenere_cipher_shifts.get(i)) % len(the_alphabet())
    message_only_alphabetic = convert_number_to_letter(letter_to_number)
    processed_text = restore_original_format(text_copy, message_only_alphabetic)
    return processed_text


def prompt_user(prompt, prompt_number):
    """Return the answer to a prompt."""
    invalid_response = True
    while invalid_response:
        try:
            if prompt_number == 1:
                answer = input(prompt)
                if answer != '1' and answer != '2' and answer != '3':
                    print()
                    raise ValueError('Invalid input! ')
                else:
                    invalid_response = False
                    return answer
            if prompt_number == 2:
                answer = input(prompt)
                if not answer.isalpha():
                    print()
                    raise ValueError('Invalid input! ')
                else:
                    invalid_response = False
                    return answer
        except ValueError as e:
            print(f'{e}')


def main():
    """Run the program."""
    print('Make your selection from the following options: ', end='\n\n')
    print('[1] - Encrypt a message')
    print('[2] - Decrypt a message')
    print('[3] - Cancel', end='\n\n', flush=True)
    choice = prompt_user('Please enter either 1, 2, or 3: ', 1)
    print()
    option = []
    if choice == '1':
        option = ['encrypt', 'encryption', 'encrypted']
    elif choice == '2':
        option = ['decrypt', 'decryption', 'decrypted']
    elif choice == '3':
        print('Goodbye!')
        return
    print(f'Please enter the message that you would like to {option[0]}: ')
    message = input()
    print()
    key = prompt_user(f'Please enter an alphabetic string for the {option[1]} key: ', 2)
    print()
    print(f'The following is your {option[2]} message: ', end='\n\n')
    print(vigenere_cipher(message, key, f'{option[0]}'))


if __name__ == "__main__":
    main()

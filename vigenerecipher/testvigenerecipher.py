from vigenerecipher import *
import pycipher


def test_convert_letter_to_number(text):
    """Return None if the assert statement is true.

    The result of the function call to convert_letter_to_number(), is compared with a list of ints that
    is constructed through using the ord() function. The ord() function returns an int that is a representation
    of a Unicode character. There is a subtraction of 97, so that the lowercase letter 'a' starts at 0, in
    accordance with the indexing of the list containing the alphabet.
    """
    assert convert_letter_to_number(text) == [ord(letter.lower()) - 97 for letter in text], 'not equal'


test_convert_letter_to_number('Python')
test_convert_letter_to_number('cryptography')
test_convert_letter_to_number('chemistry')
test_convert_letter_to_number('electroencephalography')
test_convert_letter_to_number('mountains')
print('PASS')


def test_convert_number_to_letter(numbers):
    """Return None if the assert statement is true.

    The result of the function call to convert_number_to_letter(), is compared with a string that is
    constructed from the join() function used with a list that is constructed through using the chr()
    function. The chr() function returns a str from an int that is a representation of a Unicode character.
    There is an addition of 97, so that 0 is associated with the lowercase letter 'a', in accordance with
    the indexing of the list containing the alphabet.
    """
    assert convert_number_to_letter(numbers) == ''.join([chr(number + 97) for number in numbers]), 'not equal'


test_convert_number_to_letter([15, 24, 19, 7, 14, 13])  # numeric equivalent of 'python'
test_convert_number_to_letter([2, 17, 24, 15, 19, 14, 6, 17, 0, 15, 7, 24])  # numeric equivalent of 'crytography'
test_convert_number_to_letter([2, 7, 4, 12, 8, 18, 19, 17, 24])  # numeric equivalent of 'chemistry'
test_convert_number_to_letter([4, 11, 4, 2, 19, 17, 14, 4, 13, 2, 4, 15, 7, 0, 11, 14, 6, 17, 0, 15, 7,
                               24])  # numeric equivalent of 'electroencephalography'
test_convert_number_to_letter([12, 14, 20, 13, 19, 0, 8, 13, 18])  # numeric equivalent of 'mountains'
print('PASS')

assert restore_original_format('Ice!!Cream', 'abcdefgh') == 'Abc!!Defgh', 'not equal'
assert restore_original_format('Quantum -theory', 'abcdefghijklm') == 'Abcdefg -hijklm', 'not equal'
assert restore_original_format('CrYpToGrApHy', 'abcdefghijkl') == 'AbCdEfGhIjKl', 'not equal'
assert restore_original_format('  -Python', 'abcdef') == '  -Abcdef', 'not equal'
assert restore_original_format(' P r o g r a m m i n g', 'abcdefghijk') == ' A b c d e f g h i j k', 'not equal'
print('PASS')


def test_vigenere_cipher(text, key, process):
    """Return None if the assert statement is true."""
    if process == 'encrypt':
        assert vigenere_cipher(text, key, 'encrypt') == restore_original_format(text, pycipher.Vigenere(key).encipher(text))
    elif process == 'decrypt':
        assert vigenere_cipher(text, key, 'decrypt') == restore_original_format(text, pycipher.Vigenere(key).decipher(text))


test_vigenere_cipher('Python', 'program', 'encrypt')
test_vigenere_cipher('   Cryptography ', 'code', 'encrypt')
test_vigenere_cipher('ChEmIsTry', 'science', 'encrypt')
test_vigenere_cipher('Electro - encephalography', 'neuroscience', 'encrypt')
test_vigenere_cipher('Quantum theory!!!', 'physics', 'encrypt')

test_vigenere_cipher('Ephnfn', 'program', 'decrypt')
test_vigenere_cipher('   Efbtvcjvcdkc ', 'code', 'decrypt')
test_vigenere_cipher('UjMqVuXja', 'science', 'decrypt')
test_vigenere_cipher('Rpythjq - mrpgtueffujcxll', 'neuroscience', 'decrypt')
test_vigenere_cipher('Fbyfbwe iocgza!!!', 'physics', 'decrypt')
print('PASS')

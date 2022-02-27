# Vigenère cipher: CSCI 1300 Final Project

* **Instructor:** Dr. Michael E. Cotterell
* **Semester:** Spring 2021
* **Author:** Zehadi Alam

## Introduction


<b> Encryption </b> is a method of securing information through an algorithm, such that it is rendered into a meaningless and unintelligible format. It is a form of secure communication (i.e. unintended individuals are not able to understand the message). A <b> cipher </b> is a particular encryption algorithm. Among the various ciphers that exist, I will focus here on a <b> substitution cipher </b> called the <b> Vigenère cipher</b>. A substitution cipher is an encryption algorithm that involves substituting individual characters of the <b><a href="https://en.wikipedia.org/wiki/Plaintext"> plaintext</a> </b> (non-encrypted text) with certain other characters to produce the <b><a href="https://en.wikipedia.org/wiki/Ciphertext">ciphertext</a></b> (encrypted text) (e.g. the letter "A" can be substituted with the letter "E"). The particular substitution being made is based on a key, which specifies the value for shifting from the original letter (e.g. a right-shift value of 4 when applied to the letter "A", yields the letter "E"). What we have described so far is actually a cipher known as the <b><a href="https://en.wikipedia.org/wiki/Caesar_cipher"> Caesar cipher</a></b>. The Vigenère cipher is essentially many Caesar ciphers, in that different shift values are used throughout the plaintext (i.e. one for each letter until repetition of the values are required), instead of the same shift value for every letter. <br><br>The Vigenère cipher is no longer a secure encryption algorithm and should not be used for serious encryption. It can still be used for teaching purposes. That is what is often done, as it is taught in cryptography courses during the overview of historical ciphers. Suppose that as a demonstration of the Vigenère cipher, you decide to encrypt a page-length amount of text. Doing this manually would be greatly tedious and tiresome, not to mention take a long time to do. <br><br>If you program an algorithm to carry out the task for you, it would be as simple as inputting the text you want to encrypt to the program and have the program output the encrypted text. I will proceed to explain the process of encrypting a plaintext message with the Vigenère cipher, so that one might be able to implement it themselves in their preferred programming language. <br>

## Algorithm

Encrypting a message with the Vigenère cipher requires two things:
<ul>
    <li> The message to be encrypted </li>
    <li> A key </li>
</ul>
The key in this context, refers to any alphabetic sequence of characters. The way that the key is applied in the encryption process will be explained as follows. <br>
<p align="center"><strong>Table 1</strong></p>
<div align="center"><table>
    <tr>
        <th> A </th>
        <th> B </th>
        <th> C </th>
        <th> D </th>
        <th> E </th>
        <th> F </th>
        <th> G </th>
        <th> H </th>
        <th> I </th>
        <th> J </th>
        <th> K </th>
        <th> L </th>
        <th> M </th>
        <th> N </th>
        <th> O </th>
        <th> P </th>
        <th> Q </th>
        <th> R </th>
        <th> S </th>
        <th> T </th>
        <th> U </th>
        <th> V </th>
        <th> W </th>
        <th> X </th>
        <th> Y </th>
        <th> Z </th>
     </tr>
     <tr>
        <th> 0 </th>
        <th> 1 </th>
        <th> 2 </th>
        <th> 3 </th>
        <th> 4 </th>
        <th> 5 </th>
        <th> 6 </th>
        <th> 7 </th>
        <th> 8 </th>
        <th> 9 </th>
        <th> 10 </th>
        <th> 11 </th>
        <th> 12 </th>
        <th> 13 </th>
        <th> 14 </th>
        <th> 15 </th>
        <th> 16 </th>
        <th> 17 </th>
        <th> 18 </th>
        <th> 19 </th>
        <th> 20 </th>
        <th> 21 </th>
        <th> 22 </th>
        <th> 23 </th>
        <th> 24 </th>
        <th> 25 </th>
    </tr>
</table></div>

Suppose we want to encrypt the message "Cryptology" with the key "Python" <br>
To do this, we can refer to Table 1 to map each letter in the message and the key with its numeric value, as determined by its position in the alphabet. <br><br>
"Cryptology" will be converted to: 2 17 24 15 19 14 11 14 6 24 <br>
"Python" will be converted to: 15 24 19 7 14 13 <br><br>
After the letter to number conversion, each number associated with the word "Cryptology" will be mapped to each number associated with the word "Python".<br>
If there are fewer numbers of the key than the message, then one must start over with the key numbers after all of them have been mapped to the numbers of message.<br>
In this example, the mapping of the message with the key will look like the following (notice the repetition of the key after the sixth column):
<p align="center"><strong>Table 2</strong></p>
<div align="center"><table>
    <tr>
        <th> 2 </th>
        <th> 17 </th>
        <th> 24 </th>
        <th> 15 </th>
        <th> 19 </th>
        <th> 14 </th>
        <th> 11 </th>
        <th> 14 </th>
        <th> 6 </th>
        <th> 24 </th>
    </tr>
    <tr>
        <th> 15 </th>
        <th> 24 </th>
        <th> 19 </th>
        <th> 7 </th>
        <th> 14 </th>
        <th> 13 </th>
        <th> 15 </th>
        <th> 24 </th>
        <th> 19 </th>
        <th> 7 </th>
    </tr>
</table></div>
<br>
Once the mapping, as shown by Table 2, is complete, each column value of the first row must be added with the column value of the second row. Each of the numbers of the key constitute the "shift value" for each of the numbers of the message.<br><br> For example, the first letter of the message is a "C" (numeric equivalent of 2), and the number mapped to it based on the key is 15. That means that the replacement ciphertext character will be 15 places to the right of the position of "C" in the alphabet (right-shift for encryption; left-shift for decryption). Adding 2 and 15 results in 17, which is mapped to "R", as shown in Table 1. Thus, the first character of the ciphertext for "Cryptology" with the key "Python" is "R". <br><br>For shift values that will take you past the "edge" of the alphabet, the modulo operation (denoted by "%") needs to be carried out on the sum. The sum % 26 will allow for the sum to "wrap around" the alphabet, so that the number maps on to a letter. <br><br>Following the process that we have described so far for the remaining letters, the numeric equivalent of the ciphertext for the word "Cryptology" is 17 15 17 22 7 1 0 12 25 5. When we convert this to the alphabetic ciphertext using Table 1, we get: Rprwhbamzf <br><br>
To decrypt this ciphertext back into the plaintext, follow the same process carried out on the plaintext for the ciphertext, but use subtraction for the column values, instead of addition.

## Implementation

The following code blocks contain my implementation of the Vigenère cipher. <br><br>Topics from Modules 1 - 5 that have been incorporated: <br><br><b>Module 1:</b>
<ul>
    <li> Values and expressions - Used all throughout the program.</li>
    <li> Assignment statements - Used all throughout the program.</li>
    <li> Boolean expressions - Used in every function except <code>the_alphabet()</code>
</ul>
<b> Module 2:</b>
<ul>
    <li> Boolean operators - Used in every function except <code>the_alphabet()</code> and <code>restore_original_format()</code></li>
    <li> Decision statements - Used in every function except <code>the_alphabet()</code>, <code>test_convert_letter_to_number()</code>, and <code>test_convert_number_to_letter()</code></li>
    <li> Loops - Used in every function except <code>the_alphabet()</code> and <code>main()</code></li>
    <li> F-strings - Used in <code>prompt_user()</code> and <code>main()</code></li>
</ul>
<b> Module 3:</b>
<ul>
    <li> Functions - Used in the first seven code blocks in the Implementation section and the first two code blocks in the Test Cases and Discussion section.</li>
    <li> Exception handling - Used in the functions <code>convert_letter_to_number()</code>, <code>convert_number_to_letter()</code>, and <code>prompt_user()</code></li>
    <li> String methods
        <ul>
            <li> <code>convert_letter_to_number()</code> uses <code>replace()</code> and <code>upper()</code></li>
            <li> <code>restore_original_format()</code> uses <code>isalpha()</code>, <code>isupper()</code>, <code>upper()</code>, and <code>isspace()</code></li>
            <li> <code>vigenere_cipher()</code> uses <code>lower()</code></li>
            <li> <code>prompt_user()</code> uses <code>isalpha()</code></li>
            <li> <code>test_convert_letter_to_number()</code> uses <code>lower()</code></li>
            <li> <code>test_convert_number_to_letter()</code> uses <code>join()</code></li>
        </ul>
    </li>
</ul>
<b> Module 4:</b>
<ul>
    <li> Lists - Used in every function except <code>restore_original_format()</code> and <code>prompt_user()</code>
        <ul>
            <li> List comprehension is used in <code>test_convert_letter_to_number()</code> and <code>test_convert_number_to_letter()</code>
            </li>
        </ul>
    </li>
</ul>
<b> Module 5:</b>
<ul>
    <li> Dictionaries - Used in <code>vigenere_cipher()</code></li>
</ul>


```python
def the_alphabet():
    """Return a list containing the alphabet as individual characters."""
    return ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
```


```python
def convert_letter_to_number(text):
    """Return a list with the numeric position (starting at zero) in the alphabet for each letter of the inputted argument.
    
    Example: >>> convert_letter_to_number('python')
                 [15, 24, 19, 7, 14, 13]
    """
    try:
        text_no_spaces = text.replace(' ', '') # removing whitespace
        letter_to_number = [0] * len(text_no_spaces) # initialize list with zeros
        alphabet = the_alphabet()
        k = 0
        for i in range(0, len(text)):
            for j in range(0, len(alphabet)):
                if text[i] == alphabet[j] or text[i] == alphabet[j].upper():
                    letter_to_number[k] = j # assigning index of character to list position 'k'
                    k += 1
        return letter_to_number
    except AttributeError:
        print('Invalid input! Must only input alphabetic strings.')
```


```python
def convert_number_to_letter(letter_to_number):
    """Return a string that is the alphabetic equivalent for a list of numbers.
    
    Example: >>> convert_number_to_letter([15, 24, 19, 7, 14, 13])
                 python
    """
    try:
        for i in range(0, len(letter_to_number)):
            if not isinstance(letter_to_number[i], int): # check if every element is int
                raise TypeError
        message_only_alphabetic = ''
        for i in range(0, len(letter_to_number)):
            for j in range(0, len(the_alphabet())):
                if letter_to_number[i] == j:
                    message_only_alphabetic += the_alphabet()[j] # concatenating alphabetic character
        return message_only_alphabetic
    except TypeError:
        print('Invalid input! Must only input iterables containing data of type int.')
```


```python
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
            else:
                restored_text += modified_format[j]
            j += 1
        elif original_format[i].isspace(): # accounting for spaces in original_format text
            restored_text += ' '
        else:
            restored_text += original_format[i] # accounting for other non-alphabetic characters
    return restored_text
```


```python
def vigenere_cipher(text, key, process):
    """Return the encrypted or decrypted version of inputted text, based on the process and key specified.
    
    Example: >>> vigenere_cipher('Quantum theory', 'physics', 'encrypt')
                 Fbyfbwe iocgza
                
             >>> vigenere_cipher('Fbyfbwe iocgza', 'physics', 'decrypt')
                 Quantum theory
    """
    text_copy = text # make a copy of text to be used for restoring original format later
    letter_to_number = convert_letter_to_number(text)
    vigenere_cipher_shifts = {} # dictionary for holding shift values
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
```


```python
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
```


```python
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
```


```python
if __name__ == "__main__":
    main()
```

## Test Cases and Discussion

In my implementation of the Vigenère cipher, I wanted a message that is decrypted to look the same as the original message, so I created the <code>restore_original_format()</code> function. This preserves spaces, punctuation, and other non-alphabetic characters that may have been present in the original message. I have not included an ability to remove these characters, which is a limitation of the program.

The following code blocks contain test cases of the major functions that make up my program. Although test cases are provided for functions that are not the <code>vigenere_cipher()</code> function, those functions are not meant to be called directly. They are meant to be like private utility functions and only valid inputs will ever get entered when they are called by the <code>vigenere_cipher()</code> function. Because these functions are not meant to be called directly, not all of them incorporate exception handling. The <code>restore_original_format()</code> function, for example, will throw an exception if the argument for the second parameter has more alphabetic characters than the first argument. This is not a handled exception, since attempting to handle it led to issues with preserving certain non-alphabetic characters in the original message when using the <code>vigenere_cipher()</code> function to encrypt and decrypt.

Another bug that I was not able to resolve is that when the main function is run, sometimes the prompt appears before the print statements, instead of after. This occurs intermittently and inconsistently, so I was not able to track down the cause of it.


```python
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
```


```python
def test_convert_number_to_letter(numbers):
    """Return None if the assert statement is true.
    
    The result of the function call to convert_number_to_letter(), is compared with a string that is 
    constructed from the join() function used with a list that is constructed through using the chr() 
    function. The chr() function returns a str from an int that is a representation of a Unicode character. 
    There is an addition of 97, so that 0 is associated with the lowercase letter 'a', in accordance with 
    the indexing of the list containing the alphabet.
    """
    assert convert_number_to_letter(numbers) == ''.join([chr(number + 97) for number in numbers]), 'not equal'
    
test_convert_number_to_letter([15, 24, 19, 7, 14, 13]) # numeric equivalent of 'python'
test_convert_number_to_letter([2, 17, 24, 15, 19, 14, 6, 17, 0, 15, 7, 24]) # numeric equivalent of 'crytography'
test_convert_number_to_letter([2, 7, 4, 12, 8, 18, 19, 17, 24]) # numeric equivalent of 'chemistry'
test_convert_number_to_letter([4, 11, 4, 2, 19, 17, 14, 4, 13, 2, 4, 15, 7, 0, 11, 14, 6, 17, 0, 15, 7, 24]) # numeric equivalent of 'electroencephalography'
test_convert_number_to_letter([12, 14, 20, 13, 19, 0, 8, 13, 18]) # numeric equivalent of 'mountains'
print('PASS')
```


```python
assert restore_original_format('Ice!!Cream', 'abcdefgh') == 'Abc!!Defgh', 'not equal'
assert restore_original_format('Quantum -theory', 'abcdefghijklm') == 'Abcdefg -hijklm', 'not equal'
assert restore_original_format('CrYpToGrApHy', 'abcdefghijkl') == 'AbCdEfGhIjKl', 'not equal'
assert restore_original_format('  -Python', 'abcdef') == '  -Abcdef', 'not equal'
assert restore_original_format(' P r o g r a m m i n g', 'abcdefghijk') == ' A b c d e f g h i j k', 'not equal'
print('PASS')
```


```python
# The following test cases are based on the encryption and decryption results from:
# https://www.scopulus.co.uk/tools/vigenerecipher.htm

assert vigenere_cipher('Python', 'program', 'encrypt') == 'Ephnfn', 'not equal'
assert vigenere_cipher('   Cryptography ', 'code', 'encrypt') == '   Efbtvcjvcdkc ', 'not equal'
assert vigenere_cipher('ChEmIsTry', 'science', 'encrypt') == 'UjMqVuXja', 'not equal'
assert vigenere_cipher('Electro - encephalography', 'neuroscience', 'encrypt') == 'Rpythjq - mrpgtueffujcxll', 'not equal'
assert vigenere_cipher('Quantum theory!!!', 'physics', 'encrypt') == 'Fbyfbwe iocgza!!!', 'not equal'

assert vigenere_cipher('Ephnfn', 'program', 'decrypt') == 'Python', 'not equal'
assert vigenere_cipher('   Efbtvcjvcdkc ', 'code', 'decrypt') == '   Cryptography ', 'not equal'
assert vigenere_cipher('UjMqVuXja', 'science', 'decrypt') == 'ChEmIsTry', 'not equal'
assert vigenere_cipher('Rpythjq - mrpgtueffujcxll', 'neuroscience', 'decrypt') == 'Electro - encephalography', 'not equal'
assert vigenere_cipher('Fbyfbwe iocgza!!!', 'physics', 'decrypt') == 'Quantum theory!!!', 'not equal'
print('PASS')
```


```python

```

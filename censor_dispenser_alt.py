#!/usr/bin/env python3

import string

def strip_end_punctuation(str):
    'Returns slice of string up to last (alphabetical) letter'
    last_letter_index = len(str)-1
    while last_letter_index >= 0:
        if str[last_letter_index] not in string.ascii_letters:
            last_letter_index -= 1
        else:
            break

    return str[:last_letter_index+1]

def text_to_words(text):
    '''
    Splits text string into individual words and returns list of pairs (word, index), where index is index in text where word appears
    '''
    word_list = []
    word = ''
    word_index = 0

    for i, char in enumerate(text):
        # Start of new word
        if word == '':
            if char in string.ascii_letters:
                word_index = i
                word = char
        
        # In mid-word, either add letter or reset
        else:
            if char == ' ':
                word_list.append((strip_end_punctuation(word), word_index))
                word = ''
            else:
                word += char
    
    # Add final word to list
    if word != '': word_list.append((strip_end_punctuation(word), word_index))

    return word_list
            
def text_to_words_test():
    test_text1 = 'Hello, my name is Christopher Leonard. I am testing this function.'
    test_text2 = 'This text has \'quotation marks\' '
    test_text3 = 'It\'s a possessive-apostrophe'
    test_text4 = '.f sff.. ]fs +f ,ss '

    test_output1 = text_to_words(test_text1)
    test_output2 = text_to_words(test_text2)
    test_output3 = text_to_words(test_text3)
    test_output4 = text_to_words(test_text4)

    print('Test 1:')
    print(test_output1)
    print('Test 2:')
    print(test_output2)
    print('Test 3:')
    print(test_output3)
    print('Test 4:')
    print(test_output4)

def strip_end_punctuation_test():
    strip_test1 = 'fjlkasdhu . [], []+'
    strip_test2 = ''
    strip_test3 = 'fasdh'
    strip_test4 = '\'][., +]'

    test_output1 = strip_end_punctuation(strip_test1)
    test_output2 = strip_end_punctuation(strip_test2)
    test_output3 = strip_end_punctuation(strip_test3)
    test_output4 = strip_end_punctuation(strip_test4)

    print('Test 1:')
    print(test_output1)
    print('Test 2:')
    print(test_output2)
    print('Test 3:')
    print(test_output3)
    print('Test 4:')
    print(test_output4)


# Entry point function
def main():
    # These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
    email_one = open("email_one.txt", "r").read()
    email_two = open("email_two.txt", "r").read()
    email_three = open("email_three.txt", "r").read()
    email_four = open("email_four.txt", "r").read()

    


if __name__ == '__main__':
    text_to_words_test()
    #strip_end_punctuation_test()
    main()
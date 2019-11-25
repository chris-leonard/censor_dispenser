#!/usr/bin/env python3

# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

def censor_word(text: str, word: str) -> str:
    'Replaces instances of word in text with stars of same length. Word can be a phrase (can include spaces)'
    return text.replace(word, '*' * len(word))

# Censor the word 'learning algorithms' from email one
email_one_censored = censor_word(email_one, 'learning algorithms')

def censor_words(text: str, words: list) -> str:
    'Censors each of the words (or phrases) in list'
    for word in words:
        text = censor_word(text, word)
    return text

# Censor the proprietary terms in email two
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
email_two_censored = censor_words(email_two, proprietary_terms)

# Issues:
# - Doesn't censor the s at the end of words
# - Can't deal with capitals
# - Can't deal with certain punctuation (e.g. her's)
# - Censors if it finds the word inside another one

# Entry point function
def main():
    #print('Email one censored: ' + email_one_censored)
    print('Email two censored: ' + email_two_censored)
    uncensored_text = 'My name is Chris and I am 27 years old'
    print('Uncensored string: ' + uncensored_text)
    print('Censored string: '+ censor_words(uncensored_text, ['Chris', '27']))

if __name__ == '__main__':
    main()
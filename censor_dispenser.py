#!/usr/bin/env python3

# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

def censor_word(text, word, comparison_text = None):
    '''
    Replaces instances of word or phrase (case insensitive) in text with *s - number equal to length of word.
    Optional argument allows you to search for occurances of word in comparison_text and replace them with *s at corresponding place in text.
    comparison_text must have same length as text, by default comparison_text = text.
    '''
    # Set default value of comparison text, raise error if not in expected form
    word = word.lower()
    if comparison_text is None: comparison_text = text.lower()
    if len(comparison_text) != len(text): raise ValueError('The text and comparison text must have the same length.')
    
    # Find first instance of word in comparison_text
    index = comparison_text.find(word)
    if index == -1: return text

    while True:
        # Replace word by *s in text
        text = text[: index] + '*' * len(word) + text[index + len(word):]
        
        # Find next instance of word in comparison_text
        if index == len(comparison_text) - 1: # If last index we're done
            return text
        else:
            to_next_index = comparison_text[index + 1:].find(word)
            # Test if there is another instance of word
            if to_next_index == -1:
                return text
            else:
                index += 1 + to_next_index

# Censor the word 'learning algorithms' from email one
email_one_censored = censor_word(email_one, 'learning algorithms')
print(len(email_one))

def censor_words(text: str, words: list) -> str:
    'Censors each of the words (or phrases) in list'
    # Store original text and use this to search for words
    # This removes issue of missing a word we want to censor (e.g. herself) as we have already replaced part of it (e.g. her) with stars
    censored_text = text
    for word in words:
        censored_text = censor_word(censored_text, word, comparison_text = text)
    return censored_text

# Censor the proprietary terms in email two
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
email_two_censored = censor_words(email_two, proprietary_terms)

# Issues:
# - Doesn't censor the s at the end of words
# - Can't deal with capitals (Fixed)
# - Can't deal with certain punctuation (e.g. her's)
# - Censors if it finds the word inside another one
# - It censored 'her' before 'herself' so couldn't see 'herself' - allow censor_words to compare against a different text (Fixed)

# Entry point function
def main():
    #print('Email one censored: ' + email_one_censored)
    print('Email two censored: ' + email_two_censored)
    uncensored_text = 'My name is Chris and I am 27 years old'
    print('Uncensored string: ' + uncensored_text)
    print('Censored string: '+ censor_word(uncensored_text, ['Chris', '27']))

if __name__ == '__main__':
    main()
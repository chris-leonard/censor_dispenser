#!/usr/bin/env python3

# Packages
from math import inf

def censor_word(text, word, comparison_text = None):
    '''
    Replaces instances of word or phrase (case insensitive) in text with *s - number equal to length of word.
    Optional argument allows you to search for occurances of word in comparison_text and replace them with *s at corresponding place in text.
    comparison_text must have same length as text, by default comparison_text = text.
    '''
    # Set default value of comparison text, raise error if not in expected form
    if comparison_text is None: comparison_text = text
    if len(comparison_text) != len(text): raise ValueError('The text and comparison text must have the same length.')

    word = word.lower()
    comparison_text = comparison_text.lower()
    
    # Search through instances of word in comparison_text, replace chars in text
    index = comparison_text.find(word)
    while index != -1:
        # Replace word by *s in text
        text = text[: index] + '*' * len(word) + text[index + len(word):]   
        # Find next instance of word
        index = comparison_text.find(word, index+1)
    return text

def find_from_list(str, subs, start = 0):
    '''
    Does the same as str.find(sub, start) except subs is a list of strings.
    Return the lowest index in str where a substring from subs is found within the slice [start:].
    Returns -1 if no substring is found.
    '''
    # Cycle through substrings, find lowest index where one appears
    sub_index = inf
    for sub in subs:
        try:
            sub_index = min(sub_index, str.index(sub, start))
        except ValueError:
            pass
    
    return -1 if sub_index == inf else sub_index

def censor_words(text, words, negative_words = None, neg_threshold = 0):
    '''
    Censors each of the words or phrases in the words list using censor_word
    Censors all words in the negative_words list after any negative words have been used at least 'negativity_threshold' times.
    '''
    # Store original text and use this to search for words
    # This removes issue of missing a word we want to censor (e.g. herself) as we have already replaced part of it (e.g. her) with stars
    censored_text = text
    comparison_text = text.lower()

    # Censor words in words list
    for word in words:
        censored_text = censor_word(censored_text, word, comparison_text = comparison_text)

    if negative_words is None: return censored_text

    # Find index of (neg_threshold)th negative word
    neg_index = -1
    for i in range(neg_threshold):
        neg_index = find_from_list(comparison_text, negative_words, start = neg_index+1) 
        if neg_index == -1: return censored_text
    
    # Censor negative words past neg_index
    return censored_text[:neg_index + 1] + censor_words(censored_text[neg_index + 1:], negative_words)

# Issues:
# - Doesn't censor the s at the end of words
# - Can't deal with certain punctuation (e.g. her's)
# - Censors if it finds the word inside another one

# Entry point function
def main():
    # These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
    email_one = open("email_one.txt", "r").read()
    email_two = open("email_two.txt", "r").read()
    email_three = open("email_three.txt", "r").read()
    email_four = open("email_four.txt", "r").read()

    # Censor the word 'learning algorithms' from email one
    email_one_censored = censor_word(email_one, 'learning algorithms')
    #print('Email one censored: ' + email_one_censored)

    # Censor the proprietary terms in email two
    proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
    email_two_censored = censor_words(email_two, proprietary_terms)
    print('Email two censored: ' + email_two_censored)

    # Censor negative words after they have occurred twice
    negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]
    email_three_censored = censor_words(email_three, proprietary_terms, negative_words = negative_words, neg_threshold = 2)
    #print('Email three uncensored: ' + email_three)
    print('Email three censored: ' + email_three_censored)

    # Tests:
    uncensored_text = 'aaa'
    print('Uncensored string: ' + uncensored_text)
    #print('First occurance: ' + str(find_from_list(uncensored_text, ['name', 'Chris', 'My'], start = 12)))
    print('Censored string: '+ censor_words(uncensored_text, [], negative_words = ['a'], neg_threshold = 3))

if __name__ == '__main__':
    main()
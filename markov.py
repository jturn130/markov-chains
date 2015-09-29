"""At command line provide <file_path> and <n-gram>
ex: python markov.py corpus.txt 3 --> produces 3-word Markov chains
"""
from random import choice
import sys

input_path = sys.argv[1]
n_gram = int(sys.argv[2])


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    contents = open(file_path).read()
    #implement .read

    return contents

    # all_text = ""

    # for line in file_object:
    #     all_text += line

    # print all_text       
    # return all_text

def make_chains(text_string, n):
    """Takes input text as string; returns dictionary of n-length markov chains.

    A chain will be a key that consists of a n-tuple of (word1, word2, ..., wordn)
    and the value would be a list of the word(s) that follow those n words in the
    input text.

    For example:

        >>> make_chains("hi there mary hi there juanita", 2)
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    # your code goes here
    words = text_string.split()
    # # print words

    word_key = words[:n]
    print word_key
    tuple_key = tuple(word_key)
    print "This is a tuple key: {}".format(tuple_key)

    for i in range(len(words)-n): #update range, probably n?
        # create empty list to hold n-length chain
        # iterate and append word to key list
        # to create next list: slice first item off list and append next_word
        # word_key = (words[i], words[i+1])
        if tuple_key in chains:
            chains[tuple_key].append(words[i+n]) 
        else:
            chains[tuple_key] = [words[i+n]]
        # take all of word_key except the first item
        word_key = word_key[1:]
        word_key.append(words[i+n])
        print "This is the updated word_key: {}".format(word_key)
        tuple_key = tuple(word_key)

    return chains

def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    # your code goes here

    random_key = choice(chains.keys())
    word1, word2 = random_key
    if text == "":
        text = " ".join(random_key)

    # print "This is text: {}".format(text)


    while True:
        try:    
            next_word = choice(chains[random_key])
            
            text += (" " + next_word)

            random_key = (word2, next_word)
            word2 = next_word
            # print "This is text: {}".format(text)
            # print "This is next_key: ({}, {})".format(random_key[0], random_key[1])
        except KeyError:
            break
    return text

# input_path = "green-eggs.txt"
# input_path = "gettysburg.txt"
# input_path = "kanye_lincoln.txt"
# input_path = "esb.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, n_gram)

# Produce random text
random_text = make_text(chains)

print random_text

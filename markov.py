from random import choice


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

def make_chains(text_string):
    """Takes input text as string; returns dictionary of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    # your code goes here
    words = text_string.split()
    # # print words
    for i in range(len(words)-2):
        word_key = (words[i], words[i+1])
        if word_key in chains:
            chains[word_key].append(words[i+2]) 
        else:
            chains[word_key] = [words[i+2]]

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
input_path = "kanye.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text

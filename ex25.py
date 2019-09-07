def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')    #Split a string into a list where each word is a list item, it will be splited each time a space is there
    return words                #Retunrs the new list created

def sort_words(words):
    """Sorts the words"""
    return sorted(words)        #Sorts the list "words"

def print_first_word(words):
    """Prints the first word after popping it off"""
    word = words.pop(0)         #pop() is an inbuilt function in Python that removes and returns last value from the list or the index mentioned
    print(word)

def print_last_word(words):
    """Prints the first word after popping it off"""
    word = words.pop(-1)         #pop() is an inbuilt function in Python that removes and returns last value from the list or the index mentioned
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words. """
    words = break_words(sentence)   #here the string will be partitioned in a list
    return sort_words(words)    #returns the result of the function sort_words applied to the words variable (the result of break words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence. """
    words = break_words(sentence)   #first split the sentence in a list with all the words
    print_first_word(words)         #calls the function that prints the first word
    print_last_word(words)          #calls the function that prints the last word

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one. """
    words = sort_sentence(sentence)
    print_first_word(words)         #calls the function that prints the first word
    print_last_word(words)          #calls the function that prints the last word

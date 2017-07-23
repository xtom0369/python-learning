def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

# 原方法中调用了pop方法，会破坏原来的数组，我们本意只是想打印出来而已
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words[0]
    print(f"""{word}""")

# 原方法中调用了pop方法，会破坏原来的数组，我们本意只是想打印出来而已
def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words[-1]
    print(f"""{word}""")

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

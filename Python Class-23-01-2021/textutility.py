def char_count(paragraph):
    """this function accepts a textstring and return 
    an integer count of number of character""" 
    char_count=len(paragraph)
    return char_count
def word_Count(paragraph):
    """this function accepts a textstring and return 
    an integer count of number of word""" 
    word_count = len(paragraph.split(" "))
    return word_count
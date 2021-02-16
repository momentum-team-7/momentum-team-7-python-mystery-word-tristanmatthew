STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
# 1 open file and save it to a variable - Jupyter 09
# - normalize all words to lowercase - sentence.lower
    with open(file) as open_file:
        read_file = open_file.read().lower()
# 2 remove punctuation jupyter 07
        remove_punctuation = '''!()-[]{};:'"`\,<>./?@#$%^&;*_~'''
        for char in read_file:
            if char in remove_punctuation:
                read_file = read_file.replace(char, "")

# # - remove "stop words" -- words used so frequently they are ignored
        list_of_words = read_file.split(' ')
        list_of_words_copy = list_of_words.copy()
        number_of_words = {}
        for word in list_of_words:
            if word in STOP_WORDS:
                list_of_words_copy.remove(word)
            elif word not in number_of_words:
                number_of_words_copy = list_of_words_copy.count(word)
                number_of_words[word] = number_of_words_copy

                print(number_of_words[word])
        

    print(read_file)


# check each word and see if it is equal to one of the stop words/if it is in the list of stop words
# - go through the file word by word and keep a count of how often each word is used
    # pass


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)

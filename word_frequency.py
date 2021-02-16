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

    print(read_file)


# # - remove "stop words" -- words used so frequently they are ignored
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


# needed to import string for the punctuation
import string

# Given list of stop words
STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
    'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to',
    'were', 'will', 'with'
]


# function that runs when python opens a txt file
# 'file' takes place of txt file
def print_word_freq(file):
    # with open is used to open and close the txt file when done
    with open(file, 'r') as txt_file:
        # python reads the txt file, replaces \n if necessary
        # and puts in in doc_string
        doc_string = txt_file.read().replace('\n', ' ')
        # my_punctuation is string punctuation but keeps the 
        # apostropes by cutting them out
        my_punctuation = string.punctuation.replace("'", "")
        # for in goes through and edits out any punctuation 
        for character in my_punctuation:
            doc_string = doc_string.replace(character, ' ')
        # splitting the string into a list of lowercase words
        doc_words = doc_string.lower().split()
        # filter out the stop words
        for word in STOP_WORDS:
            doc_words = list(filter((word).__ne__, doc_words))
    # create an empty dictionary to put words and count in
    txt_doc = {}
    # create entries in dictionary for each word found and how many
    for word in doc_words:
        txt_doc[word] = doc_words.count(word)
    # sorting dictionary
    srt_tuple = sorted(txt_doc.items(), key=lambda item: item[1], reverse=True)
    sorted_dict = {k: v for k, v in srt_tuple}
    # use dictiionary to gather results for printout
    for key, value in sorted_dict.items():
        stars = "*" * value
        # print results with format for each entry
        print('{:>15}{:>2}{:>3}{:^1}{:<4}'.format(key, "|", value, " ", stars))


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

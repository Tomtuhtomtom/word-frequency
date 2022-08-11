import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    with open(file, 'r') as txt_file:
        doc_string = txt_file.read().replace('\n', ' ')
        my_punctuation = string.punctuation.replace("'", "")
        for character in my_punctuation:
            doc_string = doc_string.replace(character, ' ')
        doc_words = doc_string.lower().split()
        for word in STOP_WORDS:
            doc_words = list(filter((word).__ne__, doc_words))
    txt_doc = {}
    for word in doc_words:
        txt_doc[word] = doc_words.count(word)
    for key, value in txt_doc.items():
        stars = "*" * value
        result = f'\t{key} | {value} {stars}'
        print(result.center(20, ' '))


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

import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

with open('simple-test-file.txt', 'r') as file:
    doc_string = file.read().replace('\n', ' ')
    for character in string.punctuation:
        doc_string = doc_string.replace(character, ' ')
    doc_words = doc_string.lower().split()
    for word in STOP_WORDS:
        doc_words = list(filter((word).__ne__, doc_words))


txt_doc = {}

for word in doc_words:
    txt_doc[word] = doc_words.count(word)

for key, value in txt_doc.items():
    print(key, " | ", value, ("*" * value))

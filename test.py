# Need to open txt file - check
# Need to split and lowercase all words - check
# Need to remove punctuation and stop words - punctuation check - need stop words
# Need to count number of times each word is used
# Need to print out word | # & * x #

# opening a file as a string without lines or punctuation, split and lowercased
import string

with open('one-today.txt', 'r') as file:
    doc_string = file.read().replace('\n', ' ')
    for character in string.punctuation:
        doc_string = doc_string.replace(character, ' ')
    words = doc_string.lower().split()

print(words)


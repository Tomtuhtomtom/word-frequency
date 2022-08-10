# Need to open txt file - check
# Need to split and lowercase all words - check
# Need to remove punctuation and stop words - punctuation check - need stop words
# Need to count number of times each word is used
# Need to print out word | # & * x #

# opens a file as a string without lines or punctuation, split and lowercased
# Need to manage - and 's words
import string

with open('one-today.txt', 'r') as file:
    doc_string = file.read().replace('\n', ' ')
    for character in string.punctuation:
        doc_string = doc_string.replace(character, ' ')
    words = doc_string.lower().split()

print(words)
# print(type(string.punctuation))


# testing
# list_of_words = ["hello", "world", "again", "hello", "world", "a", "the", "hello", "world", "again"]

# for word in list_of_words:
#     print(f'{word} number of times: {list_of_words.count(word)}')

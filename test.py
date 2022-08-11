# Need to open txt file - check
# Need to split and lowercase all words - check
# Need to remove punctuation and stop words - punctuation check
#    need stop words
# Need to count number of times each word is used
# Need to print out word | # & * x #

# opens a file as a string without lines or punctuation, split and lowercased
# Need to manage - and 's words
# import string

# with open('one-today.txt', 'r') as file:
#     doc_string = file.read().replace('\n', ' ')
#     for character in string.punctuation:
#         doc_string = doc_string.replace(character, ' ')
#     words = doc_string.lower().split()

# print(words)
# print(type(string.punctuation))


# testing - working list and dictionary that counts the words
# list_of_words = [
#     "hello",
#     "world",
#     "again",
#     "hello",
#     "world",
#     "a",
#     "the",
#     "hello",
#     "world",
#     "again"
#         ]

# txt_doc = {}

# for word in list_of_words:
#     txt_doc[word] = list_of_words.count(word)

# for key, value in txt_doc.items():
#     print(key, " | ", value, ("*" * value))


# testing for stop words
# STOP_WORDS = [
#     'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
#     'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to',
#     'were', 'will', 'with'
# ]

# list_of_words = [
#     "hello",
#     "world",
#     "again",
#     "hello",
#     "world",
#     "a",
#     "the",
#     "hello",
#     "world",
#     "again",
#     "the",
#     "a"
#         ]


# for word in STOP_WORDS:
#     if word in list_of_words:
#         list_of_words.remove(word)


# print(list_of_words)

# for word in STOP_WORDS:
#     list_of_words = list(filter((word).__ne__, list_of_words))


# print(list_of_words)

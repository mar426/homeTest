import string
import analysis as analysis
import inflect
from collections import Counter
import nltk
import ner as ner
from matplotlib.colors import is_color_like
from word2number import w2n


# from nltk.tag.stanford import StanfordNERTagger
# st = NERTagger('stanford-ner/all.3class.distsim.crf.ser.gz', 'stanford-ner/stanford-ner.jar')


file = open("dickens.txt", "tr")
# file = open("file.txt", "tr")
data = file.read()
# print(data)


# 1:
def split_text(data):
    data = data.replace("-", " ")
    return data.split()


# 2:
def num_of_lines():
    num_lines = sum(1 for line in open('dickens.txt'))
    return num_lines


# 3:
# cleaning
def clean_text(data):
    data = data.lower()
    data = data.replace("'s", '')  # remove 's
    data = data.replace("-", " ")  # remove -
    for i in string.punctuation:
        data = data.replace(i, " ")  # remove all Punctuation
    return data.strip().split()  # remove \n and split to words


# print(len(clean_text(data)))


# finding unique
def unique_words(word_list):
    unique_words_list = set(word_list)
    # print(unique_words_list)
    return len(unique_words_list)


# 4:
def length_sentences(data):
    sentences = data.split('.')  # split for sentences
    avg_len = sum(len(x.split()) for x in sentences) / len(sentences)
    max_len = max(len(i.split()) for i in sentences)
    return avg_len, max_len


# 5:
def most_popular_word(data):
    counter1 = Counter(clean_text(data))  # count number of appear per words
    most_occur = counter1.most_common(1)  # take the most common word
    return most_occur


def most_popular_syntactic(data):
    tokens = nltk.word_tokenize(data)  # divide the words as tokenize
    # print("len(tokens):", len(tokens))
    tagged = nltk.pos_tag(tokens)  # detect every token type
    tagged = tagged[:]
    # filtering of syntactic words:
    tagged = [i[0] for i in tagged if i[1] != 'DT' and i[1] != 'IN' and i[1] != 'CC' and i[1] != 'VBP' and i[1] != 'PRP$' and i[1] != 'TO']
    # print(len(tagged))
    str1 = ' '.join(str(x) for x in tagged)
    counter1 = Counter(clean_text(str1))
    most_occur = counter1.most_common(1)
    # print("tagged:", tagged)
    return most_occur

# print(most_popular_syntactic(data))


# 6:
def length_without_k(data):
    notK = []
    for i in split_text(data):
        if 'k' in i:
            notK.append('##')  # replace every words with k to '##'
        else:
            notK.append(i)
    new_data = ' '.join(map(str, notK))
    new_list = new_data.split('##')  # divide to words sequences without k
    new_list = [i.split() for i in new_list]
    str1 = ' '.join(str(x) for x in max(new_list, key=len))
    maxS = max(new_list, key=len)
    return len(maxS), str1


# 7:
def text2int(textnum, numwords={}):
    if not numwords:
        units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
        ]

        tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

        scales = ["hundred", "thousand", "million", "billion", "trillion"]

        numwords["and"] = (1, 0)
        for idx, word in enumerate(units):  numwords[word] = (1, idx)
        for idx, word in enumerate(tens):       numwords[word] = (1, idx * 10)
        for idx, word in enumerate(scales): numwords[word] = (10 ** (idx * 3 or 2), 0)

    ordinal_words = {'first': 1, 'second': 2, 'third': 3, 'fifth': 5, 'eighth': 8, 'ninth': 9, 'twelfth': 12}
    ordinal_endings = [('ieth', 'y'), ('th', '')]

    textnum = textnum.replace('-', ' ')

    current = result = 0
    curstring = ""
    onnumber = False
    for word in textnum.split():
        if word in ordinal_words:
            scale, increment = (1, ordinal_words[word])
            current = current * scale + increment
            if scale > 100:
                result += current
                current = 0
            onnumber = True
        else:
            for ending, replacement in ordinal_endings:
                if word.endswith(ending):
                    word = "%s%s" % (word[:-len(ending)], replacement)

            if word not in numwords:
                if onnumber:
                    curstring += repr(result + current) + " "
                curstring += word + " "
                result = current = 0
                onnumber = False
            else:
                scale, increment = numwords[word]

                current = current * scale + increment
                if scale > 100:
                    result += current
                    current = 0
                onnumber = True

    if onnumber:
        curstring += repr(result + current)

    return curstring


# numbers = []
# intText = text2int(data)
# for i in intText.split():
#     if i.isnumeric():
#        numbers.append(i)
# print(intText)
# print("max number:", max(numbers))

# 8:
def color_in_text(data):
    colors_list = [i for i in clean_text(data) if is_color_like(i)]  # using in color library of python
    return colors_list


# 9:
def find_characters_in_text(data):
    character = []
    sentences = data.split('.')
    sentences = [i.split() for i in sentences]
    # print(sentences)
    # choosing the relevant words:
    for i in sentences:
        for j in i[1:]:
            if j[0].isupper():
                character.append(j)
    str1 = ' '.join(str(x) for x in character)
    # checking if it's characters:
    tokens = nltk.word_tokenize(str1)
    tagged = nltk.pos_tag(tokens)
    tagged = tagged[:]
    tagged = [i[0] for i in tagged if i[1] == 'NNP']
    print(tagged)
    # print(len(tagged))
    str1 = ' '.join(str(x) for x in tagged)
    counter1 = Counter(clean_text(str1))
    most_occur = counter1.most_common(1)
    return most_occur


# printing results:
print("1) words:", len(split_text(data)))
print("2) rows:", num_of_lines())
print("3) uniques: ", unique_words(clean_text(data)))
print("4) length average:", length_sentences(data)[0], ", max length:", length_sentences(data)[1])
print("5) *", most_popular_word(data))
print("  **", most_popular_syntactic(data))
print("6)", length_without_k(data)[1], "\n length:",  length_without_k(data)[0])
print("8)", Counter(color_in_text(data)))
# print("9)", find_characters_in_text(data))

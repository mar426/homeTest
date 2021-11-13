import string
import inflect
from collections import Counter
from matplotlib.colors import is_color_like
from word2number import w2n
import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
p = inflect.engine()
p.number_to_words(99)
print(str(p))

sentence = """I am you are they and do not that the feel very good."""
tokens = nltk.word_tokenize(sentence)
print(tokens)
tagged = nltk.pos_tag(tokens)
print(tagged[:])


file = open("dickens.txt", "tr")
data = file.read()
print(data)


# 1:
def split_text(data):
    data = data.replace("-", " ")
    return data.split()


# 2:
num_lines = sum(1 for line in open('dickens.txt'))


# 3:
# cleaning
def clean_text(data):
    data = data.lower()
    data = data.replace("'s", '')
    data = data.replace("-", " ")
    for i in string.punctuation:
        data = data.replace(i, " ")
    return data.strip().split()


print(len(clean_text(data)))


def unique_words(word_list):
    # finding unique
    unique = []
    for word in word_list:
        if word not in unique:
            unique.append(word)
    # print("unique a:", unique)
    return len(unique)


# 4:
def length_sentences(data):
    sentences = data.split('.')
    avg_len = sum(len(x.split()) for x in sentences) / len(sentences)
    max_len = max(len(i.split()) for i in sentences)
    return avg_len, max_len


# 5:
def most_popular_word(data):
    # text = [i.lower() for i in data]
    counter1 = Counter(clean_text(data))
    most_occur = counter1.most_common(1)
    return most_occur


def most_popular_syntactic(data):
    # text = [i.lower() for i in data]
    tokens = nltk.word_tokenize(clean_text(data))
    print("len(tokens):", len(tokens))
    tagged = nltk.pos_tag(tokens)
    tagged = tagged[:]
    tagged = [i[0] for i in tagged if i[1] != 'DT' or i[1] != 'IN' or i[1] != 'CC' or i[1] != 'VBP']
    print("tagged:", tagged)


# most_popular_syntactic(data)
# 6:
def length_without_k(data):
    notK = []
    for i in split_text(data):
        if 'k' in i:
            notK.append('##')
        else:
            notK.append(i)
    new_data = ' '.join(map(str, notK))
    bb = new_data.split('##')
    bb = [i.split() for i in bb]
    str1 = ' '.join(str(x) for x in max(bb, key=len))
    maxS = max(bb, key=len)
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
    colors_list = [i for i in clean_text(data) if is_color_like(i)]
    return colors_list


# 9:
# sentences = data.split('.')
# sentences = [i.split() for i in sentences]
# print(sentences)

# printing results:
print("1) words:", len(split_text(data)))
print("2) rows:", num_lines)
# print("3) uniques: ", unique_words(clean_text(data)))
print("4) length average:", length_sentences(data)[0], "max length:", length_sentences(data)[1])
print("5)", most_popular_word(data))
print("6)", length_without_k(data)[1], "\n length:",  length_without_k(data)[0])
print("8)", Counter(color_in_text(data)))


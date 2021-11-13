import string
num_lines = 0
data = []
cleanText = []
unique = []
with open("dickens.txt.") as infile:
    for line in infile:
        num_lines += 1
        transLine = str.maketrans('', '', string.punctuation)
        cleanLine = [word.replace("'s", '') for word in line.split()]
        cleanLine = [word.translate(transLine) for word in cleanLine]
        cleanLine = [word.strip() for word in cleanLine]
        for i in cleanLine:
            cleanText.append(i)
            if i not in unique:
                unique.append(i)
        for i in line.split():
            data.append(i)


print(cleanText)
print(len(cleanText))
print(num_lines)
print("3) uniques: ", len(unique))



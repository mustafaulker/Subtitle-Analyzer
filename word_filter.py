# Reading stopwords.txt file's content
with open('lists/stopwords.txt', encoding='utf8') as infile:
    stopwords_list = infile.readlines()
infile.close()

stopwords = []

# Separate words and assign them as list element.
for line in stopwords_list:
    stopwords += line.split()


# Filter input list with stopwords.
def filter_stopwords(to_be_filtered):
    return [i for i in to_be_filtered if i not in set(stopwords)]

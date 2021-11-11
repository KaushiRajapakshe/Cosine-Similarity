# !pip install nltk
# import nltk
# nltk.download('all')


# Program to measure the similarity between
# two sentences using cosine similarity.
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def similarity(sentence1, sentence2):

    # tokenization
    sentence1_list = word_tokenize(sentence1)
    sentence2_list = word_tokenize(sentence2)

    # sw contains the list of stopwords
    sw = stopwords.words('english')
    l1 = []
    l2 = []

    # remove stop words from the string
    sentence1_set = {w for w in sentence1_list if not w in sw}
    sentence2_set = {w for w in sentence2_list if not w in sw}

    # form a set containing keywords of both strings
    rvector = sentence1_set.union(sentence2_set)
    for w in rvector:
        if w in sentence1_set:
            l1.append(1)  # create a vector
        else:
            l1.append(0)
        if w in sentence2_set:
            l2.append(1)
        else:
            l2.append(0)
    c = 0

    # cosine formula
    for i in range(len(rvector)):
        c += l1[i] * l2[i]
    cosine = c / float((sum(l1) * sum(l2)) ** 0.5)
    return cosine

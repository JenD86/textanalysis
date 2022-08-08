from collections import defaultdict
import os

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import manhattan_distances, cosine_similarity
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
import matplotlib.pyplot as plt

mydir = 'round1_1'

def create_original_docs(mydir):
    char_array = dict()
    for filename in filter(lambda x: x[-4:] == '.txt', os.listdir(mydir)):
        char_array[filename] = list(open(os.path.join(mydir, filename), 'r', encoding='utf-8').read())

    chars_docs_sorted = []
    s_count = 0
    for s in sorted(char_array.keys()):
        print(str(s_count) + ': ' + s)
        chars_docs_sorted.append(' '.join(char_array[s]))
        s_count+=1
    return chars_docs_sorted


def create_common_char_docs(mydir):
    char_array = dict()
    for filename in filter(lambda x: x[-4:] == '.txt', os.listdir(mydir)):
        char_array[filename] = list(open(os.path.join(mydir, filename), 'r', encoding='utf-8').read())

    common_chars = set.intersection(*[set(i) for i in list(char_array.values())])

    common_chars_array = defaultdict(dict)
    common_chars_docs = defaultdict(list)
    for doc in char_array.keys():
        for c in common_chars:
            common_chars_array[doc][c] = char_array[doc].count(c)
            common_chars_docs[doc].extend(char_array[doc].count(c)*c)

    common_chars_docs_sorted = []
    s_count = 0
    for s in sorted(common_chars_docs.keys()):
        print(str(s_count) + ': ' + s)
        common_chars_docs_sorted.append(' '.join(common_chars_docs[s]))
        s_count+=1

    return (common_chars_array, common_chars_docs_sorted, sorted(common_chars_docs.keys()), common_chars)

def create_excluded_char_docs(mydir, excluded_chars=[]):
    char_array = dict()
    for filename in filter(lambda x: x[-4:] == '.txt', os.listdir(mydir)):
        char_array[filename] = list(open(os.path.join(mydir, filename), 'r', encoding='utf-8').read())
    
    excluded_chars_array = dict()
    for filename in char_array.keys():
        excluded_chars_array[filename] = ' '.join(list(filter(lambda c: c not in excluded_chars, char_array[filename])))
    excluded_chars_docs_sorted = []
    fn_count = 0
    for filename in sorted(excluded_chars_array.keys()):
        print(str(fn_count) + ': ' + filename)
        excluded_chars_docs_sorted.append(excluded_chars_array[filename])
        fn_count+=1

    return (excluded_chars_array, excluded_chars_docs_sorted, sorted(excluded_chars_array.keys()))

def read_docs_into_cv_cosine_similarity_matrix(docs):
    cv = CountVectorizer(token_pattern=r"(?u)\b\w+\b")
    fitted = cv.fit_transform(docs).todense()
    cosine_similarity_matrix = cosine_similarity(fitted, fitted)
    return cosine_similarity_matrix

def read_docs_into_tfidf_cosine_similarity_matrix(docs):
    tfidf = TfidfVectorizer(token_pattern=r"(?u)\b\w+\b")
    fitted = tfidf.fit_transform(docs).todense()
    cosine_similarity_matrix = cosine_similarity(fitted, fitted)
    return cosine_similarity_matrix

def read_docs_into_dendrogram(docs, method='complete', vectorizer='cv', metric='euclidean', threshold=0.1):
    if vectorizer == 'cv':
        v = CountVectorizer(token_pattern=r"(?u)\b\w+\b")
    elif vectorizer == 'tfidf':
        v = TfidfVectorizer(token_pattern=r"(?u)\b\w+\b")
    else:
        v = CountVectorizer(token_pattern=r"(?u)\b\w+\b")
    fitted = v.fit_transform(docs).todense()
    linkages = linkage(fitted, method, metric=metric)
    dn = dendrogram(linkages)
    plt.show()
    return fcluster(linkages, threshold, criterion="distance")

#def read_docs_into_tfidf_euclidean_dendrogram(docs, method='weighted', threshold=0.1):
#    tfidf = TfidfVectorizer()
#    fitted = tfidf.fit_transform(docs).todense()
#    linkages = linkage(fitted, method, metric="euclidean")
#    dn = dendrogram(linkages)
#    plt.show()
#    return fcluster(linkages, threshold, criterion="distance")
#
#def read_docs_into_cv_euclidean_dendrogram(docs, method='weighted', threshold=0.1):
#    tfidf = TfidfVectorizer()
#    fitted = tfidf.fit_transform(docs).todense()
#    linkages = linkage(fitted, method, metric="euclidean")
#    dn = dendrogram(linkages)
#    plt.show()
#    return fcluster(linkages, threshold, criterion="distance")
#
#def read_docs_into_cv_manhattan_dendrogram(docs, method='weighted', threshold=0.1):
#    cv = CountVectorizer()
#    fitted = cv.fit_transform(docs).todense()
#    linkages = linkage(fitted, method, metric="cityblock")
#    dn = dendrogram(linkages)
#    plt.show()
#    return fcluster(linkages, threshold, criterion="distance")
#
#

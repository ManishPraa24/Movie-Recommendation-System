## This module will calculate the similarity score matrix.

# In case you want to generate the same similarity score matrix as of mine,
# then you can use this module.

import nltk
from nltk.stem.porter import PorterStemmer

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity



ps = PorterStemmer()

def stem(text):

    y = []

    for i in text.split():
        y.append(ps.stem(i))

    return " ".join(y)


def similarity_scores(dataFrame, max_features = 5000, stop_words = 'english'):

    cv = CountVectorizer(max_features=max_features, stop_words=stop_words)

    dataFrame['tags'] = dataFrame['tags'].apply(stem)

    tag_vectors = cv.fit_transform(dataFrame['tags']).toarray()

    similarity_score_matrix = cosine_similarity(tag_vectors)

    return similarity_score_matrix


### OriginalsByM24
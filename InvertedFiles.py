import os
from collections import defaultdict
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')

def preprocess(text):
    text = text.lower()
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in tokens if word.isalnum() and word not in stop_words]
    return words

documents = {}

for filename in os.listdir():
    if filename.endswith(".txt"):
        with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
            text = f.read()
            documents[filename] = preprocess(text)

print(f"Total documents loaded: {len(documents)}")

inverted_index = defaultdict(set)

for doc_id, words in documents.items():
    for word in set(words):
        inverted_index[word].add(doc_id)

print(f"Vocabulary size: {len(inverted_index)} words")

print("\nSample inverted index terms:")
for term in list(inverted_index)[:30]:
    print(f"{term}: {sorted(inverted_index[term])}")

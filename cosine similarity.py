from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#create TFI IDF
vectorizer=TfidfVectorizer()
#fit and transform documents
tfidf_matrix=vectorizer.fit_transform(documents)
print("Vocabulary",vectorizer.get_feature_names_out())
print("TF_IDF Matrix:\n",tfidf_matrix.toarray())

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
nltk.download('punkt')
nltk.download('stopwords')
def preprocess_text(text):
    text = text.lower()
    words = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in filtered_words]
    return stemmed_words
text = "Machine Learning are revolutionizing the world of AI"
print("Original Text:",text)
process = preprocess_text(text)
processed_text = ' '.join(process)
print("Processed Text: ",processed_text)
print("Preprocessed words: ",process)

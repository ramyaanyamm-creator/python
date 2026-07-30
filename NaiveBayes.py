from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score,classification_report
categories = ['sci.space','rec.sport.hockey','comp.graphics','alt.atheism']
newsgroups = fetch_20newsgroups(subset = 'all',categories = categories,shuffle= True,random_state = 42)
print(f"Total Documents: {len(newsgroups.data)}")
print(f"Target Classes: {newsgroups.target_names}")
x_train,x_test,y_train,y_test = train_test_split(newsgroups.data,newsgroups.target,test_size=0.2,random_state = 42)
vectorizer = TfidfVectorizer(stop_words = 'english')
x_train_tfid = vectorizer.fit_transform(x_train)
x_test_tfid = vectorizer.transform(x_test)
nb = MultinomialNB()
nb.fit(x_train_tfid,y_train)
y_pred = nb.predict(x_test_tfid)
print("Accuracy: ",accuracy_score(y_test,y_pred))
print("\n Classification Report: \n")
print(classification_report(y_test,y_pred,target_names=newsgroups.target_names))
for i in range(5):
    print("\nTest:\n",x_test[i])
    print("Actual",newsgroups.target_names[y_test[i]])
    print("Predicted:",newsgroups.target_names[y_pred[i]])

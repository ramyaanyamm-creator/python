import numpy as np
from scipy.stats import mode

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import precision_score, recall_score, f1_score

categories = [
    'alt.atheism',
    'comp.graphics',
    'sci.space',
    'talk.religion.misc'
]

newsgroups = fetch_20newsgroups(
    subset='all',
    categories=categories,
    remove=('headers', 'footers', 'quotes')
)

vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
X = vectorizer.fit_transform(newsgroups.data)

y_true = newsgroups.target

k = len(categories)
kmeans = KMeans(n_clusters=k, random_state=42)
y_pred = kmeans.fit_predict(X)

print("\n========== CLUSTERING RESULTS ==========\n")

for cluster in range(k):
    print(f"\nCluster {cluster + 1}")
    print("-" * 50)

    cluster_docs = np.where(y_pred == cluster)[0]

    print(f"Number of documents: {len(cluster_docs)}\n")

    # Show first 5 documents in the cluster
    for doc_id in cluster_docs[:5]:
        print(f"Document {doc_id}")
        print(newsgroups.data[doc_id][:250].replace("\n", " "))
        print()

def purity_score(y_true, y_pred):
    clusters = np.unique(y_pred)
    classes = np.unique(y_true)

    contingency_matrix = np.zeros((len(clusters), len(classes)))

    for i, cluster in enumerate(clusters):
        indices = np.where(y_pred == cluster)[0]
        true_labels = y_true[indices]

        if len(true_labels) == 0:
            continue

        most_common = mode(true_labels, keepdims=True).mode[0]
        count = np.sum(true_labels == most_common)

        j = np.where(classes == most_common)[0][0]
        contingency_matrix[i][j] = count

    return np.sum(np.max(contingency_matrix, axis=1)) / np.sum(contingency_matrix)

def map_clusters_to_labels(y_true, y_pred):
    label_mapping = {}

    for cluster in np.unique(y_pred):
        indices = np.where(y_pred == cluster)[0]

        if len(indices) == 0:
            continue

        majority_label = mode(y_true[indices], keepdims=True).mode[0]
        label_mapping[cluster] = majority_label

    mapped_preds = np.array([label_mapping[cluster] for cluster in y_pred])
    return mapped_preds
y_pred_mapped = map_clusters_to_labels(y_true, y_pred)
purity = purity_score(y_true, y_pred)
precision = precision_score(y_true, y_pred_mapped, average='macro')
recall = recall_score(y_true, y_pred_mapped, average='macro')
f1 = f1_score(y_true, y_pred_mapped, average='macro')
print("\n========== EVALUATION METRICS ==========")
print("Purity Score :", round(purity, 4))
print("Precision    :", round(precision, 4))
print("Recall       :", round(recall, 4))
print("F1-Score     :", round(f1, 4))

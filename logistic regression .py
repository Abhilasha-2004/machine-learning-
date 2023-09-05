import numpy as np
from sklearn.datasets import load_wine  
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


wine = load_wine()
X = wine.data
y = wine.target


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


model = LogisticRegression()


model.fit(X_train, y_train)


y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')


report = classification_report(y_test, y_pred, target_names=wine.target_names)
print('Classification Report:\n', report)

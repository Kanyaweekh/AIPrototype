# train_model.py
import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# 1. Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# 2. Initialize and train the Random Forest Classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X, y)

# 3. Save the model to a file
joblib.dump(clf, 'iris_model.pkl')

print("Model trained and saved as 'iris_model.pkl'")
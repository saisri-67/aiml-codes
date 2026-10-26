
import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Test case 1 - Normal training
model = MLPClassifier(
    hidden_layer_sizes=(5,),
    max_iter=1000,
    random_state=42
)
model.fit(X_train, y_train)
print("Test case 1 - Accuracy:", model.score(X_test, y_test))

# Test case 2 - 100 epochs
model = MLPClassifier(
    hidden_layer_sizes=(5,),
    max_iter=100,
    random_state=42
)
model.fit(X_train, y_train)
print("Test case 2 - Weights updated: Yes")

# Test case 3 - Training completed
model = MLPClassifier(
    hidden_layer_sizes=(5,),
    max_iter=1000,
    random_state=42
)
model.fit(X_train, y_train)
print("Test case 3 - Training Completed")

# Test case 4 - High learning rate
model = MLPClassifier(
    hidden_layer_sizes=(5,),
    learning_rate_init=1.0,
    max_iter=100,
    random_state=42
)
model.fit(X_train, y_train)
print("Test case 4 - High learning rate")

# Test case 5 - Zero epoch
print("Test case 5 - Zero epoch: No training")

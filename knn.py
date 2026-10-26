
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training Samples:", len(X_train))
print("Testing Samples:", len(X_test))

# TEST CASE 1: Valid K
print("\nTest Case 1: Valid K")
k = 3

if k <= 0:
    print("Error: K must be greater than 0")
elif k > len(X_train):
    print("Error: K is larger than training dataset")
else:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)

    print("Test Case: K =", k)
    print("Actual labels:")
    print(y_test)
    print("Predicted labels:")
    print(y_pred)

    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)
    print("Accurate Classification" if accuracy >= 0.8
          else "Classification needs improvement")

# TEST CASE 2: K = 0
print("\nTest Case 2: K = 0")

k = 0
if k <= 0:
    print("Error: K must be greater than 0")

# TEST CASE 3: K = -1
print("\nTest Case 3: K = -1")

k = -1
if k <= 0:
    print("Error: K must be greater than 0")

# TEST CASE 4: K larger than training dataset
print("\nTest Case 4: K larger than training dataset")

k = 200
if k <= 0:
    print("Error: K must be greater than 0")
elif k > len(X_train):
    print("Error: K is larger than training dataset")
    print("Please choose K <=", len(X_train))

# TEST CASE 5: Valid K = 1
print("\nTest Case 5: K = 1")

k = 1
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification completed")

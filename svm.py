
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.svm import SVC, OneClassSVM
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load Iris dataset
iris = load_iris()
X = iris.data[:, :2]
y = iris.target

# Use two classes for linear SVM visualization
X = X[y != 2]
y = y[y != 2]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train SVM model
svm = SVC(kernel="linear", C=1)
svm.fit(X_train, y_train)

# Display results
print("Accuracy:", svm.score(X_test, y_test))
print("Support vectors:")
print(svm.support_vectors_)

# Test point near the margin
test = X_test[0].reshape(1, -1)
decision = svm.decision_function(test)
prediction = svm.predict(test)

print("\nTest point:", test)
print("Decision value:", decision[0])
print("Prediction:", prediction[0])

# Plot decision boundary and margins
plt.figure(figsize=(8, 6))

plt.scatter(
    X_train[:, 0], X_train[:, 1],
    c=y_train, cmap="coolwarm", label="Training data"
)

ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

xx = np.linspace(xlim[0], xlim[1], 200)
yy = np.linspace(ylim[0], ylim[1], 200)
YY, XX = np.meshgrid(yy, xx)

grid = np.c_[XX.ravel(), YY.ravel()]
Z = svm.decision_function(grid).reshape(XX.shape)

plt.contour(
    XX, YY, Z,
    levels=[-1, 0, 1],
    colors=["black", "blue", "black"],
    linestyles=["--", "-", "--"]
)

plt.scatter(
    svm.support_vectors_[:, 0],
    svm.support_vectors_[:, 1],
    s=150, facecolors="none", edgecolors="green",
    label="Support vectors"
)

plt.scatter(
    test[0, 0], test[0, 1],
    marker="x", s=150, color="red", label="Test point"
)

plt.xlabel("Sepal length (scaled)")
plt.ylabel("Sepal width (scaled)")
plt.title("Linear SVM - Iris Dataset")
plt.legend()
plt.grid()
plt.show()

# Test case: overlapping classes
overlap_model = SVC(kernel="linear", C=1)
overlap_model.fit(X_train, y_train)
print("\nOverlapping class accuracy:",
      overlap_model.score(X_test, y_test))

# Test case: single-class training using One-Class SVM
single_class = X_train[y_train == 0]
scaler_one = StandardScaler()
single_class = scaler_one.fit_transform(single_class)

one_class_svm = OneClassSVM(kernel="linear", nu=0.1)
one_class_svm.fit(single_class)

test_single = scaler_one.transform(X_test[:1])
print("Single-class SVM prediction:",
      one_class_svm.predict(test_single))

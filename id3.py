import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.preprocessing import LabelEncoder
def run(data, features, name):
    df = pd.DataFrame(data, columns=features +["Target"])
    X = df.iloc[:, :-1].copy()
    y = df.iloc[:, -1].copy()
    for col in X.columns:
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col].astype(str))
    le_y = LabelEncoder()
    y = le_y.fit_transform(y.astype(str))
    model = DecisionTreeClassifier(
        criterion="entropy",
        random_state=42
    )
    model.fit(X, y)
    print("\n" + "=" * 5000)
    print(name)
    print("=" * 5000)
    print("\nDecision Tree Rules:")
    print(export_text(model, feature_names=features))
    print("Tree Depth:", model.get_depth())
    print("Number of Leaves:", model.get_n_leaves())
# Test Case 1: Play Tennis Dataset
features = ["Outlook", "Temperature", "Humidity", "Wind"]
play_tennis = [
    ["Sunny", "Hot", "High", "Weak", "No"],
    ["Sunny", "Hot", "High", "Strong", "No"],
    ["Overcast", "Hot", "High", "Weak", "Yes"],
    ["Rain", "Mild", "High", "Weak", "Yes"],
    ["Rain", "Cool", "Normal", "Weak", "Yes"],
    ["Rain", "Cool", "Normal", "Strong", "No"],
    ["Overcast", "Cool", "Normal", "Strong", "Yes"],
    ["Sunny", "Mild", "High", "Weak", "No"],
    ["Sunny", "Cool", "Normal", "Weak", "Yes"],
    ["Rain", "Mild", "Normal", "Weak", "Yes"],
    ["Sunny", "Mild", "Normal", "Strong", "Yes"],
    ["Overcast", "Mild", "High", "Strong", "Yes"],
    ["Overcast", "Hot", "Normal", "Weak", "Yes"],
    ["Rain", "Mild", "High", "Strong", "No"]
]
run(play_tennis, features, "Test Case 1: Play Tennis")
# Test Case 2: Clear Class Separation
clear_data = [
    [1, 10, "A"],
    [2, 20, "A"],
    [3, 30, "A"],
    [8, 80, "B"],
    [9, 90, "B"],
    [10, 100, "B"]
]
run(clear_data, ["Feature1", "Feature2"],
    "Test Case 2: Clear Class Separation")
# Test Case 3: Mixed Attributes
mixed_data = [
    ["Low", 20, "No"],
    ["Low", 25, "No"],
    ["Medium", 30, "Yes"],
    ["Medium", 35, "Yes"],
    ["High", 40, "Yes"],
    ["High", 45, "Yes"]
]
run(mixed_data, ["Level", "Age"],
    "Test Case 3: Mixed Attributes")
# Test Case 4: Same Class
same_class = [
    [1, "Yes"],
    [2, "Yes"],
    [3, "Yes"],
    [4, "Yes"],
    [5, "Yes"]
]
run(same_class, ["Feature"],
    "Test Case 4: Same Class")
# Test Case 5: Missing Attribute
missing_data = [
    ["Sunny", "Hot", "High", "Weak", "No"],
    ["Rain", "Mild", None, "Weak", "Yes"],
    ["Overcast", "Cool", "Normal", "Strong", "Yes"]
]
try:
    run(missing_data, features,
        "Test Case 5: Missing Attribute")
except Exception as e:
    print("\n" + "=" * 500)
    print("Test Case 5: Missing Attribute")
    print("=" * 500)
    print("Error:", e)
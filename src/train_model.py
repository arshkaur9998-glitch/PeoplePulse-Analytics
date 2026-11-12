import pandas as pd
import numpy as np
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score
)

# Load Dataset
df = pd.read_csv(
    "data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv"
)

# Remove Unnecessary Columns
df.drop(
    columns=[
        "EmployeeNumber",
        "EmployeeCount",
        "Over18",
        "StandardHours"
    ],
    inplace=True
)

# Separate Features and Target
X = df.drop("Attrition", axis=1)
y = df["Attrition"].map({"No": 0, "Yes": 1})

# Identify Column Types
categorical_columns = X.select_dtypes(
    include=["object"]
).columns

numeric_columns = X.select_dtypes(
    exclude=["object"]
).columns

# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"),
         categorical_columns),
        ("num", "passthrough", numeric_columns)
    ]
)

# Split Data: Train, Validation and Test
X_train_val, X_test, y_train_val, y_test = train_test_split(
    X, y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

X_train, X_val, y_train, y_val = train_test_split(
    X_train_val, y_train_val,
    test_size=0.25,
    random_state=42,
    stratify=y_train_val
)

# Build Model
model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("classifier", RandomForestClassifier(
            n_estimators=300,
            random_state=42,
            class_weight="balanced_subsample",
            min_samples_leaf=2
        ))
    ]
)

# Train Model
model.fit(X_train, y_train)

# Find Best Decision Threshold Using Validation Data
val_probabilities = model.predict_proba(X_val)[:, 1]

best_threshold = 0.5
best_f1 = 0

for threshold in np.arange(0.10, 0.51, 0.01):

    val_predictions = (
        val_probabilities >= threshold
    ).astype(int)

    score = f1_score(
        y_val,
        val_predictions,
        zero_division=0
    )

    if score > best_f1:
        best_f1 = score
        best_threshold = threshold

# Final Evaluation on Unseen Test Data
test_probabilities = model.predict_proba(X_test)[:, 1]

test_predictions = (
    test_probabilities >= best_threshold
).astype(int)

# Display Results
print("\nPEOPLEPULSE IMPROVED ATTRITION MODEL")
print("-----------------------------------")

print(f"Accuracy: {accuracy_score(y_test, test_predictions) * 100:.2f}%")

print(f"Selected Threshold: {best_threshold:.2f}")

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        test_predictions,
        target_names=["No", "Yes"],
        zero_division=0
    )
)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, test_predictions))

# Save Model and Threshold
os.makedirs("models", exist_ok=True)

joblib.dump(
    {
        "model": model,
        "threshold": best_threshold
    },
    "models/attrition_model.pkl"
)

print("\nImproved Model Saved Successfully!")
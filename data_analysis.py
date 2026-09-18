import pandas as pd
df = pd.read_csv("data/Telco-Customer-Churn.csv")
print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.isnull().sum())
print(df["Churn"].value_counts())
print(df.isnull().sum())
print(df.dtypes)
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

print(df.isnull().sum())
df = df.dropna()

print(df.isnull().sum())
print(df.shape)
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

print(df.isnull().sum())

df = df.dropna()

print(df.isnull().sum())
print(df.shape)
df = df.drop("customerID", axis=1)

print(df.shape)
print(df.columns)

print(df.shape)
print(df.columns)

df = pd.get_dummies(df, drop_first=True, dtype=int)

print(df.head())
print(df.shape)
X = df.drop("Churn_Yes", axis=1)
y = df["Churn_Yes"]

print(X.shape)
print(y.shape)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(X_train.shape)
print(X_test.shape)
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(y_pred[:10])
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))
from sklearn.metrics import roc_auc_score

y_prob = model.predict_proba(X_test)[:, 1]

auc = roc_auc_score(y_test, y_prob)

print("ROC-AUC:", auc)
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)

print("Confusion Matrix:")
print(cm)
import matplotlib.pyplot as plt
import seaborn as sns

sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")

plt.show()
from sklearn.tree import DecisionTreeClassifier

dt_model = DecisionTreeClassifier(random_state=42)

dt_model.fit(X_train, y_train)

dt_pred = dt_model.predict(X_test)

print("Decision Tree Accuracy:", accuracy_score(y_test, dt_pred))
from sklearn.ensemble import RandomForestClassifier

rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

rf_model.fit(X_train, y_train)

rf_pred = rf_model.predict(X_test)

print("Random Forest Accuracy:", accuracy_score(y_test, rf_pred))
print("Logistic Regression:", accuracy_score(y_test, y_pred))
print("Decision Tree:", accuracy_score(y_test, dt_pred))
print("Random Forest:", accuracy_score(y_test, rf_pred))
from sklearn.metrics import classification_report

print(classification_report(y_test, rf_pred))
importance = pd.Series(rf_model.feature_importances_, index=X.columns)

print(importance.sort_values(ascending=False).head(10))
importance.sort_values(ascending=False).head(10).plot(kind="bar")

plt.title("Top 10 Important Features")
plt.xlabel("Features")
plt.ylabel("Importance")

plt.show()
def predict_churn(customer_data):
    prediction = rf_model.predict(customer_data)
    probability = rf_model.predict_proba(customer_data)[0][1]

    return prediction[0], probability
sample_customer = X_test.iloc[[0]]

prediction, probability = predict_churn(sample_customer)

print("Churn Prediction:", prediction)
print("Churn Probability:", probability)
import joblib

joblib.dump(rf_model, "churn_model.pkl")

print("Model saved successfully!")
import joblib

joblib.dump(rf_model, "churn_model.pkl")

print("Model saved successfully!")
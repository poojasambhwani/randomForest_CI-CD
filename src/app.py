import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

df=pd.read_csv("data/attrition.csv")

df1 = df.drop(columns=["EmployeeCount", "EmployeeNumber", "StandardHours", "Over18"])

label_encoders = {}
for column in df1.select_dtypes(include='object').columns:
    lb = LabelEncoder()
    df1[column] = lb.fit_transform(df1[column])
    label_encoders[column] = lb

x = df1.drop(columns = ['Attrition'], axis = 1)
y = df1['Attrition']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

rf = RandomForestClassifier()
rf.fit(x_train, y_train)

# Predict on the test set
y_pred = rf.predict(x_test)

# Calculate evaluation metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f"Accuracy: {accuracy:}")
print(f"Precision: {precision:}")
print(f"Recall: {recall:}")
print(f"F1 Score: {f1:}")

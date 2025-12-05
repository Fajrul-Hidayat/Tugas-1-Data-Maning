import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("diet_recommendations_dataset (1).csv")

print("Jumlah Data:", len(df))
df.head()

# Pisah 70% training, 30% sisanya
train_df, temp_df = train_test_split(df, test_size=0.30, random_state=42)

# Pisah 30% menjadi validation 15% dan test 15%
validation_df, test_df = train_test_split(temp_df, test_size=0.50, random_state=42)

print("Jumlah Train:", len(train_df))
print("Jumlah Validation:", len(validation_df))
print("Jumlah Test:", len(test_df))


# Ganti 'diet_type' jika berbeda
target_col = "diet_type"

X_train = train_df.drop(target_col, axis=1)
y_train = train_df[target_col]

X_val = validation_df.drop(target_col, axis=1)
y_val = validation_df[target_col]

X_test = test_df.drop(target_col, axis=1)
y_test = test_df[target_col]


model = DecisionTreeClassifier()

# Training
model.fit(X_train, y_train)

y_pred_val = model.predict(X_val)
val_acc = accuracy_score(y_val, y_pred_val)

print("Akurasi Validation:", val_acc)

y_pred_test = model.predict(X_test)
test_acc = accuracy_score(y_test, y_pred_test)

print("Akurasi Test:", test_acc)

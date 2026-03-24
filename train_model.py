import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
df = pd.read_csv('data/loan_data.csv')

# Features & target
X = df.drop('approved', axis=1)
y = df['approved']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train RandomForest model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save trained model
with open('model/loan_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved successfully!")

import pandas as pd
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
from sklearn.metrics import classification_report

# Load the dataset
data = pd.read_csv('DATASET/tic_tac_toe_training_weighted.csv')

# Features (board positions)
X = data[[f'pos{i}' for i in range(1, 10)]]

# Target (best move)
y = data['move']

# Define sample weights (favoring winning moves)
weights = data['score'].replace({-1: 60, 0: 6, 1: 4})




# Split the data to evaluate generalization (important!)
X_train, X_test, y_train, y_test, w_train, w_test = train_test_split(
    X, y, weights, test_size=0.15, random_state=42
)

# Initialize the model
model = lgb.LGBMClassifier(
    n_estimators=400,
    learning_rate=0.05,
    num_leaves=25,
    max_depth=6
)

# Train (fit) the model
model.fit(X_train, y_train, sample_weight=w_train)

# Predict on test set
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

print(classification_report(y_test, y_pred))

# Save the trained model
joblib.dump(model, "DATASET/tictactoe_model.pkl")
print("Model saved successfully as tictactoe_model.pkl!")

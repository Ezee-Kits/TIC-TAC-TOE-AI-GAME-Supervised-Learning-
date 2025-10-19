import lightgbm as lgb
import joblib













# Load the model
model = joblib.load("DATASET/tictactoe_model.pkl")


# Make a new prediction
new_prediction = model.predict([[-1,0,-1,0,-1,1,0,1,1]])
print("AI NEXT MOVE IS :", new_prediction)



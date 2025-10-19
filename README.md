# 🎮 TIC-TAC-TOE-AI-GAME-Supervised-Learning

An AI-powered **Tic Tac Toe Game** built using **Supervised Machine Learning (LightGBM)**.  
The model is trained on all possible board states and predicts the **best next move** for the AI player in real time.

---

## 🧠 Overview

This project uses **data generation + machine learning + model prediction** to teach an AI how to play Tic Tac Toe intelligently.

### Workflow
1. **Generate dataset** of all possible board states and their outcomes.
2. **Train a LightGBM model** to predict the best move for each state.
3. **Load the trained model** and let the AI play automatically.

---

## ⚙️ How It Works

### 1️⃣ Data Generation

File: `TicTacToe_Data_Generator.py`

- Generates every possible 3x3 Tic Tac Toe board (3⁹ = 19,683 states).
- Filters for **valid game progressions** (turn order respected).
- Calculates each move’s **score**:
  - `-1` → AI wins
  - `1` → Player wins
  - `0` → Draw or ongoing game

The dataset is saved as:
DATASET/tic_tac_toe_training_weighted.csv


**Example of generated data:**
| pos1 | pos2 | pos3 | pos4 | pos5 | pos6 | pos7 | pos8 | pos9 | move | score |
|------|------|------|------|------|------|------|------|------|------|--------|
| -1 | 0 | 1 | 0 | -1 | 0 | 1 | 0 | 0 | 2 | 0 |
| 1 | 0 | -1 | 0 | 1 | 0 | -1 | 0 | 0 | 4 | -1 |

---

### 2️⃣ Model Training

File: `TicTacToe_Model_Trainer.py`

- Loads the generated dataset.
- Uses **LightGBM Classifier** for supervised learning.
- Assigns **weights** to emphasize winning states.
- Splits data into **training and test sets (85/15)**.
- Trains and evaluates the model.
- Saves model as:


DATASET/tictactoe_model.pkl


**Training Output Example:**


Model Accuracy: 96.78%
Model saved successfully as tictactoe_model.pkl!


---

### 3️⃣ Gameplay & Prediction

File: `TicTacToe_AI_Player.py`

- Loads the trained model.
- Takes a board state as input:
  - `-1` → AI move
  - `1` → Player move
  - `0` → Empty space
- Predicts **best next move position** (1–9).

**Example:**

```python
import joblib

model = joblib.load("DATASET/tictactoe_model.pkl")

# Current board state
# -1 = AI, 1 = Player, 0 = Empty
board = [-1, 0, -1, 0, -1, 1, 0, 1, 1]

# Predict the next move
prediction = model.predict([board])
print("AI NEXT MOVE IS :", prediction)


Output:

AI NEXT MOVE IS : [2]


That means the AI recommends position 2 as the best next move.

🧮 Machine Learning Logic Explained (Layman’s Terms)

The AI learns by observing thousands of Tic Tac Toe boards and which moves led to wins, losses, or draws.

It’s like teaching a child by showing what happens when they move in certain spots.

After enough examples, it predicts the smartest move for any given situation.

Real-world analogy:
Imagine having a friend who’s seen every possible Tic Tac Toe game ever — they instantly know the move that gives the highest chance to win.

🧰 Tech Stack
Component	Technology
Language	Python 3.10+
Model	LightGBM (Gradient Boosted Decision Trees)
Libraries	Pandas, Scikit-learn, Joblib
Dataset	Generated programmatically (no external data)
Training Approach	Supervised Learning
Task Type	Multi-class classification (9 possible moves)
📂 Folder Structure
TIC-TAC-TOE-AI-GAME-Supervised-Learning/
│
├── DATASET/
│   ├── tic_tac_toe_training_weighted.csv
│   └── tictactoe_model.pkl
│
├── TIC_TAC_TOE_Data_Generator.py     # Generates training dataset
├── TIC_TAC_TOE_Model_Trainer.py      # Trains LightGBM model
├── TIC_TAC_TOE_AI_Player.py          # Loads model and plays automatically
├── README.md                         # Documentation (this file)

⚙️ Setup & Installation
1️⃣ Clone the Repository
git clone https://github.com/EzeeKits/TIC-TAC-TOE-AI-GAME-Supervised-Learning.git
cd TIC-TAC-TOE-AI-GAME-Supervised-Learning

2️⃣ Install Dependencies
pip install pandas lightgbm scikit-learn joblib

3️⃣ Generate the Dataset
python TIC_TAC_TOE_Data_Generator.py

4️⃣ Train the Model
python TIC_TAC_TOE_Model_Trainer.py

5️⃣ Play the Game with AI
python TIC_TAC_TOE_AI_Player.py

🧩 Example Use Case
Scenario	Description
🎮 Training	The model learns from every possible game configuration.
🧠 Prediction	The AI identifies the best next move for the current state.
⚔️ Challenge	You can modify the board and challenge the AI to play optimally.
🔄 Expansion	Could be extended to Reinforcement Learning or Deep Learning models.
📊 Example Output
✅ Dataset saved as DATASET/tic_tac_toe_training_weighted.csv with 17234 rows
Model Accuracy: 21.72%
AI NEXT MOVE IS : [2]

💡 Real-Life Application

This project demonstrates how machine learning can be applied to simple games to make intelligent decisions.
It’s a foundational example for:

AI Game Development

Reinforcement Learning concepts

Pattern recognition in decision systems

Teaching supervised learning to beginners

🧠 Possible Improvements

Implement a GUI (Tkinter or Pygame) for interactive play.

Integrate reinforcement learning (Q-learning) for self-learning AI.

Visualize win/loss prediction heatmaps.

Deploy as a web app using Flask/Streamlit.

Add model retraining as AI plays new games.

👨‍💻 Author

Ezee Kits
🎓 Electrical & Electronics Engineer | Python & ML Developer
📺 YouTube Channel

📧 Email: ezeekits@gmail.com

💡 Passionate about teaching Python, Tech, and Automation

📜 License

MIT License

MIT License

Copyright (c) 2025 Ezee Kits

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...

🌟 Support

If you find this helpful:

⭐ Star this repository on GitHub

📺 Subscribe to Ezee Kits on YouTube

💬 Share feedback or contribute improvements

🧩 Summary
Step	File	Purpose
1️⃣	TIC_TAC_TOE_Data_Generator.py	Generates all board states
2️⃣	TIC_TAC_TOE_Model_Trainer.py	Trains the LightGBM model
3️⃣	TIC_TAC_TOE_AI_Player.py	Predicts best move for AI
✅	Output	Fully automated, intelligent Tic Tac Toe AI

🎯 Final Output Example:

AI NEXT MOVE IS : [2]


Your AI just made its next winning move!

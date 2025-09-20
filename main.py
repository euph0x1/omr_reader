import json
import sqlite3
import pandas as pd
from omr_utils import preprocess_image, detect_bubbles


# Load answer key
with open("data/answer_key.json") as f:
    answer_key = json.load(f)

# Subjects order
subjects = ["Python", "EDA", "MySQL", "PowerBI", "Stats"]

# Step 1: Process OMR
img, thresh = preprocess_image("data/img1.jpeg")
detected_answers = detect_bubbles(thresh)

# Step 2: Compare with answer key
results = {}
start = 0
total_score = 0

for sub in subjects:
    correct = answer_key[sub]
    student_sub_answers = detected_answers[start:start+20]
    start += 20
    
    score = 0
    for sa, ca in zip(student_sub_answers, correct):
        if sa is None:
            # Fallback to RF if needed
            # features = extract_features(...) # you’d implement
            # sa = predict_with_rf(features)
            sa = "?"  # placeholder if no RF
        if sa == ca:
            score += 1
    results[sub] = score
    total_score += score

results["Total"] = total_score

# Step 3: Save results
df = pd.DataFrame([results])
df.to_csv("results/results.csv", mode="a", header=False, index=False)

conn = sqlite3.connect("results/results.db")
df.to_sql("scores", conn, if_exists="append", index=False)
conn.close()

print("✅ Evaluation Complete:", results)

# 📄 Automated OMR Evaluation & Scoring System

## 🚩 Problem Statement
Manual checking of Optical Mark Recognition (OMR) sheets is:
- Time-consuming  
- Error-prone  
- Difficult to scale for large batches of students  

This project automates the **evaluation and scoring of OMR answer sheets**, reducing human effort while improving accuracy and consistency.

---

## 🔍 Approach
The system processes scanned OMR sheets and evaluates them automatically:

1. **Preprocessing** – Images are cleaned and aligned using **OpenCV**.  
2. **Bubble Detection** – Filled bubbles are detected through contour analysis.  
3. **Answer Comparison** – Detected responses are compared with a predefined **answer key**.  
4. **Scoring** – Per-subject and total scores are calculated.  
5. **Storage** – Results are exported into both **CSV** and **SQLite database** formats for easy reporting.  

---

## ⚙️ Tech Stack
- **Python 3.x**  
- **OpenCV** – Image preprocessing & bubble detection  
- **Pandas** – Data handling and CSV export  
- **SQLite** – Storing evaluated results  

---

## 🛠️ Installation

Follow these steps to set up the project locally:

```bash
# 1. Clone the repository
git clone https://github.com/your-username/omr_reader.git
cd omr_reader

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Prepare input data
# Place scanned OMR sheets in:
data/
# Place answer key as JSON in:
data/answer_key.json
```

▶️ Usage

Run the following command to evaluate answer sheets:
```
python main.py
```
+ Results will be saved in:
  + results/results.csv
  + results/results.db (SQLite database)

Example console output:
```
Processing OMR_Sheet_01.png ...
Score: 42/50
Results saved to results/results.csv and results/results.db
```

## 📂 Repository Structure
```bash
.
├── config/          # Answer keys or configuration files
├── data/            # OMR images + JSON answer key
├── results/         # Output CSV + SQLite DB
├── utils/           # Helper modules (preprocessing, detection, scoring)
├── main.py          # Entry point
├── requirements.txt # Project dependencies
└── README.md        # Project documentation
```

## 🚀 Future Work

+ Deploy as an interactive Streamlit web app

+ Improve accuracy with ML-based bubble detection

+ Support for different OMR sheet formats

+ Add web-based dashboard for visual analytics

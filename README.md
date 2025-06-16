# 🎓 StudentResultAnalyzer — Analyze Past Results & Predict Next Year’s Average

This project analyzes **student marks for the last 2 years**, calculates grade distributions, top performers, and predicts next year’s average marks using simple linear regression in Python with `pandas` and `scikit-learn`.

## 📁 Project Files

- `analyze_results.py` — Main Python script to load data, analyze, and predict  
- `student_results.csv` — CSV file containing student marks for the past two years  
- `requirements.txt` — List of required Python libraries

## ✅ How It Works

### 1. Load Student Data

The script reads `student_results.csv` with columns:

| Name   | Roll | Year | Marks |
|--------|------|------|-------|
| Alice  | 101  | 2023 | 88    |
| Bob    | 102  | 2023 | 73    |
| Carol  | 103  | 2024 | 90    |

You can replace this file with your own data if needed.

### 2. Analyze Data

- Convert marks into grades (A, B, C, D, F) based on marks ranges  
- Calculate how many students achieved each grade per year  
- Calculate average marks per year  
- Identify top 3 students overall

### 3. Predict Next Year’s Average

- Use **linear regression** to model average marks per year  
- Predict the average marks expected for the next year (e.g., 2025)

## 🚀 How To Run

```bash
git clone https://github.com/yourusername/StudentResultAnalyzer.git
cd StudentResultAnalyzer
pip install -r requirements.txt
python analyze_results.py
```

## 🧪 Example Output

```
Grade Distribution:
A: 1
B: 2
C: 1
...

Average Marks by Year:
2023: 75.4
2024: 78.2

Top 3 Students:
Carol (90 marks)
Alice (88 marks)
David (85 marks)

Predicted Average for 2025: 80.3
```

## 📊 Requirements

- Python 3.x  
- pandas  
- scikit-learn

## 📝 Author

Created by **A S M Tauhid Rahman** to demonstrate basic data analysis and prediction with Python.

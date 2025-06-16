This project analyzes student marks for the last 2 years, calculates grade distributions, top performers, and predicts next year’s average marks using simple linear regression in Python with pandas and scikit-learn.
# 📁 Project Files 
analyze_results.py — Main Python script to load data, analyze, and predict  
student_results.csv — CSV file containing student marks for the past two years  
requirements.txt — List of required Python libraries  
# ✅ How It Works 
# 1. Load Student Data The script reads student_results.csv with columns:  

# 2. Analyze Data 
Convert marks into grades (A, B, C, D, F) based on marks ranges  
Calculate how many students achieved each grade per year  
Calculate average marks per year  
Identify top 3 students overall  
# 3. Predict Next Year’s Average Use linear regression to model average marks per year  
Predict the average marks expected for the next year (e.g., 2025)  

#🚀 How To Run 

# 1. Clone the Repository
git clone https://github.com/yourusername/StudentResultAnalyzer.git
cd StudentResultAnalyzer
# 2. Install Dependencies
pip install -r requirements.txt
# 3. Run the Script
# 📊 Requirements
Python 3.x

pandas

scikit-learn

# 📝 Author
Created by Suchi to demonstrate basic data analysis and prediction with Python.


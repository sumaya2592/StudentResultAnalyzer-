import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('student_results.csv')

# Convert Marks to Grades
def get_grade(m):
    if m >= 80:
        return 'A'
    elif m >= 70:
        return 'B'
    elif m >= 60:
        return 'C'
    elif m >= 50:
        return 'D'
    else:
        return 'F'

df['Grade'] = df['Marks'].apply(get_grade)

# Grade Distribution
grade_counts = df['Grade'].value_counts()
print("Grade Distribution:")
print(grade_counts)

# Average Marks by Year
avg_marks = df.groupby('Year')['Marks'].mean()
print("\nAverage Marks by Year:")
print(avg_marks)

# Top 3 Students
top_students = df.sort_values(by='Marks', ascending=False).head(3)
print("\nTop 3 Students:")
print(top_students[['Name', 'Marks']])

# Prediction of next year's average
X = df.groupby('Year')['Marks'].mean().index.values.reshape(-1, 1)
y = df.groupby('Year')['Marks'].mean().values

model = LinearRegression()
model.fit(X, y)

next_year = [[max(df['Year']) + 1]]
predicted_avg = model.predict(next_year)
print(f"\nPredicted Average for {next_year[0][0]}: {predicted_avg[0]:.2f}")


import pandas as pd


# Load the student marks
data = pd.read_csv("student_marks.csv")

marks = data["Marks"].dropna()

# Calculate the descriptive statistics
mean_mark = marks.mean()
median_mark = marks.median()
mode_mark = marks.mode()
mark_range = marks.max() - marks.min()

variance = marks.var(ddof=0)
standard_deviation = marks.std(ddof=0)

# Display the results
print("Descriptive Statistics")
print("======================")
print(f"Number of students: {len(marks)}")
print(f"Mean: {mean_mark:.2f}")
print(f"Median: {median_mark:.2f}")
print(f"Mode: {', '.join(map(str, mode_mark.tolist()))}")
print(f"Range: {mark_range:.2f}")
print(f"Population variance: {variance:.2f}")
print(f"Population standard deviation: {standard_deviation:.2f}")


"""
Descriptive Statistical Analysis of Student Marks

This script calculates and explains the mean, median, mode,
range, population variance, and population standard deviation.
"""

import csv
import math
import statistics
from pathlib import Path


def load_marks():
    """Read student marks from the CSV dataset."""
    file_path = Path(__file__).parent / "student_marks.csv"

    with file_path.open(mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        if not reader.fieldnames or "Marks" not in reader.fieldnames:
            raise ValueError("The CSV file must contain a 'Marks' column.")

        marks = []

        for row in reader:
            try:
                mark = float(row["Marks"])
            except (ValueError, TypeError):
                raise ValueError("The dataset contains an invalid mark.")

            if not math.isfinite(mark) or not 0 <= mark <= 100:
                raise ValueError("Marks must be between 0 and 100.")

            marks.append(mark)

    if not marks:
        raise ValueError("The dataset contains no student marks.")

    return marks


def main():
    marks = load_marks()
    n = len(marks)

    # Calculate descriptive statistics
    total_sum = sum(marks)
    mean_value = statistics.mean(marks)
    median_value = statistics.median(marks)
    mode_values = statistics.multimode(marks)

    minimum_mark = min(marks)
    maximum_mark = max(marks)
    mark_range = maximum_mark - minimum_mark

    squared_deviations = [(mark - mean_value) ** 2 for mark in marks]
    sum_squared_deviations = sum(squared_deviations)

    population_variance = statistics.pvariance(marks)
    population_std_dev = statistics.pstdev(marks)

    # Display the analysis
    print("=" * 50)
    print("STUDENT MARKS STATISTICAL ANALYSIS")
    print("=" * 50)

    print(f"Dataset: {marks}")
    print(f"Number of students (N): {n}\n")

    print("--- 1. Mean ---")
    print(f"Sum of marks = {total_sum:.2f}")
    print(f"Mean = {total_sum:.2f} / {n} = {mean_value:.2f}\n")

    print("--- 2. Median ---")
    print(f"Sorted marks: {sorted(marks)}")
    print(f"Median = {median_value:.2f}\n")

    print("--- 3. Mode ---")
    print(f"Mode(s): {', '.join(f'{value:g}' for value in mode_values)}\n")

    print("--- 4. Range ---")
    print(f"Highest mark = {maximum_mark:g}")
    print(f"Lowest mark = {minimum_mark:g}")
   print(f"Range = {mark_range:g}\n")
    print("--- 5. Population Variance and Standard Deviation ---")
    print(f"Sum of squared deviations = {sum_squared_deviations:.2f}")
    print(
        f"Population variance = {sum_squared_deviations:.2f} / {n} "
        f"= {population_variance:.2f}"
    )
    print(
        f"Population standard deviation = "
        f"sqrt({population_variance:.2f}) = {population_std_dev:.2f}"
    )

    print("=" * 50)


if __name__ == "__main__":
    main()

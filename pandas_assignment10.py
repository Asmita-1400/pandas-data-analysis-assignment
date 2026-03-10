# =====================================================
# Assignment 10: Pandas (Series, DataFrame, Analysis)
# =====================================================

import pandas as pd


# =====================================================
# Task 1: Pandas Series Basics
# =====================================================

print("\n--- Task 1: Pandas Series Basics ---")

marks = [78, 85, 90, 66, 72]

marks_series = pd.Series(marks)

print("Series Values:\n", marks_series.values)
print("Index:\n", marks_series.index)
print("Data Type:\n", marks_series.dtype)

print("First Element:", marks_series.iloc[0])
print("Last Two Elements:\n", marks_series.tail(2))


# =====================================================
# Task 2: Mathematical Operations on Series
# =====================================================

print("\n--- Task 2: Mathematical Operations ---")

print("Add 5 Marks:\n", marks_series + 5)
print("Subtract 2 Marks:\n", marks_series - 2)
print("Multiply by 1.05:\n", marks_series * 1.05)
print("Divide by 2:\n", marks_series / 2)


# =====================================================
# Task 3: Python Functionalities on Series
# =====================================================

print("\n--- Task 3: Series Analysis ---")

print("Maximum Marks:", marks_series.max())
print("Minimum Marks:", marks_series.min())
print("Sum of Marks:", marks_series.sum())
print("Mean Marks:", marks_series.mean())

# Check pass (>=70)
passed = marks_series.apply(lambda x: x >= 70)
print("Passed Students:\n", passed)

print("Number of Students Passed:", passed.sum())


# =====================================================
# Task 4: Create a DataFrame
# =====================================================

print("\n--- Task 4: DataFrame Creation ---")

students = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks': [78, 85, 90, 66, 72],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}

df = pd.DataFrame(students)

print("First 3 Rows:\n", df.head(3))
print("Last 2 Rows:\n", df.tail(2))
print("Shape:", df.shape)
print("Columns:", df.columns)


# =====================================================
# Task 5: Important DataFrame Functions
# =====================================================

print("\n--- Task 5: DataFrame Functions ---")

print("\nInfo:")
print(df.info())

print("\nDescription:\n", df.describe())

print("\nHead:\n", df.head())
print("\nTail:\n", df.tail())

# Sort by Marks descending
df_sorted = df.sort_values(by='Marks', ascending=False)

print("\nSorted by Marks (Descending):\n", df_sorted)

# Reset index
df_sorted = df_sorted.reset_index(drop=True)
print("\nAfter Reset Index:\n", df_sorted)


# =====================================================
# Task 6: Filtering & Conditional Selection
# =====================================================

print("\n--- Task 6: Filtering ---")

print("\nMarks > 75:\n", df[df['Marks'] > 75])

print("\nSubject = Math:\n", df[df['Subject'] == 'Math'])

average_marks = df['Marks'].mean()
print("\nMarks > Average:\n", df[df['Marks'] > average_marks])

print("\nFailed Students (Marks < 70):\n", df[df['Marks'] < 70])


# =====================================================
# Task 7: Grouping & Basic Analysis
# =====================================================

print("\n--- Task 7: Grouping & Analysis ---")

print("\nAverage Marks per Subject:\n",
      df.groupby('Subject')['Marks'].mean())

print("\nCount per Subject:\n",
      df.groupby('Subject')['Name'].count())

print("\nMaximum Marks per Subject:\n",
      df.groupby('Subject')['Marks'].max())


# =====================================================
# Task 8: Pandas Plotting (Simple Graphs)
# =====================================================

print("\n--- Task 8: Plotting ---")

# Bar graph: Names vs Marks
df.plot(x='Name', y='Marks', kind='bar',
        title='Student Marks')

# Line graph of marks
df['Marks'].plot(kind='line', title='Marks Line Graph')

# Histogram
df['Marks'].plot(kind='hist', title='Marks Distribution')


# =====================================================
# Task 9: Mini Use Case - Sales Data Analysis
# =====================================================

print("\n--- Task 9: Sales Data Analysis ---")

sales = {
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    'Revenue': [1200, 1500, 900, 2000, 1800]
}

sales_df = pd.DataFrame(sales)

print("Total Revenue:", sales_df['Revenue'].sum())
print("Average Revenue:", sales_df['Revenue'].mean())

# Day with highest revenue
max_day = sales_df.loc[sales_df['Revenue'].idxmax()]
print("Highest Revenue Day:\n", max_day)

# Days where revenue > average
avg_revenue = sales_df['Revenue'].mean()
print("Revenue > Average:\n",
      sales_df[sales_df['Revenue'] > avg_revenue])

# Plot revenue vs day
sales_df.plot(x='Day', y='Revenue',
              kind='bar', title='Revenue per Day')

print("\nAssignment Completed Successfully ✅")
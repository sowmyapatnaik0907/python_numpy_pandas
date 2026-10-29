
import pandas as pd

# Create a Pandas Series
marks = pd.Series(
    [95, 92, 89, 85, 80],
    index=["Rank1", "Rank2", "Rank3", "Rank4", "Rank5"]
)

print("Student Marks:")
print(marks)

# Access the first rank student using integer position
print("First rank mark:", marks.iloc[0])

# Retrieve top three ranks using labels
print(marks.loc[["Rank1", "Rank2", "Rank3"]])

# Retrieve the third rank student
print("Third rank mark:", marks.iloc[2])

# Filter marks greater than 90
print("Marks greater than 90:")
print(marks[marks > 90])

# Modify first rank mark
marks.loc["Rank1"] = 100
print("After modification:")
print(marks)

# Remove last rank
marks = marks.drop("Rank5")
print("After removing Rank5:")
print(marks)

# Calculate CGPA
cgpa = marks / 10
print("CGPA:")
print(cgpa)

# Create the transactions DataFrame
transactions = pd.DataFrame({
    "TransactionID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "ProductCategory": [
        "Electronics", "Clothing", "Electronics", "Furniture",
        "Clothing", "Electronics", "Furniture", "Clothing",
        "Furniture", "Electronics"
    ],
    "Region": [
        "North", "South", "North", "East", "West",
        "North", "East", "West", "South", "North"
    ],
    "Amount": [200, 150, 300, 450, 200, 250, 300, 180, 350, 400]
})

# Display DataFrame
print(transactions)

# Basic exploration
print("First five rows:")
print(transactions.head())

print("Last five rows:")
print(transactions.tail())

print("Shape:", transactions.shape)
print("Column names:", transactions.columns)
print("Data types:")
print(transactions.dtypes)

# Display selected columns
print(transactions[["ProductCategory", "Amount"]])

# Retrieve the last three columns
print(transactions.iloc[:, -3:])

# Filter North region with amount greater than 200
filtered = transactions[
    (transactions["Region"] == "North") &
    (transactions["Amount"] > 200)
]
print("Filtered transactions:")
print(filtered)

# Count product categories
print("Product category counts:")
print(transactions["ProductCategory"].value_counts())

# Unique regions
print("Unique regions:")
print(transactions["Region"].unique())

# Average amount by region
print("Average amount by region:")
print(transactions.groupby("Region")["Amount"].mean())

# Modify transaction 102 amount
transactions.loc[
    transactions["TransactionID"] == 102, "Amount"
] = 165

print("After modifying transaction 102:")
print(transactions)

# Add Discount column
transactions["Discount"] = transactions["Amount"] * 0.10
print("After adding Discount:")
print(transactions)

# Remove transaction 109
transactions = transactions[
    transactions["TransactionID"] != 109
]
print("After removing transaction 109:")
print(transactions)

# Delete Discount column
transactions = transactions.drop(columns=["Discount"])
print("Final DataFrame:")
print(transactions)

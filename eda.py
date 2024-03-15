import pandas as pd
import subprocess
# Load the dataset
df = pd.read_csv("results/res_dpre.csv") 

# Basic statistics
summary_statistics = df.describe()

# Data types of columns
column_data_types = df.dtypes

# Number of missing values in each column
missing_values = df.isnull().sum()

# Unique values in categorical columns
unique_values_categorical = {col: df[col].unique() for col in df.select_dtypes(include=['object']).columns}

# Correlation between numerical columns
correlation_matrix = df[["Fare","Age"]].corr()

# Insights
insights = []

# Example insights:
# Insight 1: Summary statistics
insights.append("Insight 1: Summary Statistics\n" + str(summary_statistics))

# Insight 2: Data Types
insights.append("Insight 2: Data Types\n" + str(column_data_types))

# Insight 3: Missing Values
insights.append("Insight 3: Missing Values\n" + str(missing_values))

# Insight 4: Unique Values in Categorical Columns
for col, values in unique_values_categorical.items():
    insights.append(f"Insight 4: Unique Values in {col}\n{values}")

# Insight 5: Correlation Matrix
insights.append("Insight 5: Correlation Matrix\n" + str(correlation_matrix))

# Save insights as text files
for i, insight in enumerate(insights, start=1):
    with open(f"results/eda-in-{i}.txt", "w") as file:
        file.write(insight)

print("Calling vis.py...")
subprocess.run(["python3", "vis.py"])

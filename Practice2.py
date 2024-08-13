import pandas as pd
import os

# totals the sum of all posts per programming language, and then sorted from lowest to highest amount.

# Change the working directory
os.chdir('C:\\Users\\Siris\\Desktop\\GitHub Projects 100 Days NewB\\_24_0077__Day73_Data_Visualization_with_Matplotlib__240812\\NewProject\\r00-r09 START\\r00_env_START')

# Load the CSV file into a DataFrame
df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)

# Group by 'TAG' and sum the 'POSTS', then sort by the summed 'POSTS' in ascending order
tag_totals_sorted = df.groupby('TAG')['POSTS'].sum().sort_values()

# Print the sorted totals
print(tag_totals_sorted)

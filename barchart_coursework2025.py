import pandas as pd
import matplotlib.pyplot as plt

# File path to the final cleaned data
final_file = R'C:/Users/ksia/python programme/coursework/stripped_final_population.csv'

#Load the cleaned dataset
try:
    data = pd.read_csv(final_file)
except FileNotFoundError:
    print("Error: Final file not found. Please check the file path.")
    exit()
except Exception as e:
    print(f"Error reading the file: {e}")
    exit()

# Make sure the columns exist
if 'Species' not in data.columns or 'Cleaned Population Estimate' not in data.columns:
    print("Error: Required columns 'Species' or 'Cleaned Population Estimate' not found in the dataset.")
    exit()

# Make sure the population estimate column contains numeric values)
data['Cleaned Population Estimate'] = pd.to_numeric(data['Cleaned Population Estimate'], errors='coerce')


# Filter out rows with NaN values in the 'Cleaned Population Estimate' column
data_clean = data.dropna(subset=['Cleaned Population Estimate']).copy()  # Make a copy of the filtered data

#Ensure 'Species' column is of type string (necessary for plotting)
data_clean['Species'] = data_clean['Species'].astype(str)  # use .loc[] or .copy() to avoid the setting with copy warning error


#Create the bar chart
plt.figure(figsize=(12, 8))
plt.bar(data_clean['Species'], data_clean['Cleaned Population Estimate'], color='pink')

#Add titles and labels
plt.title('Comparison of Species and Population Estimates', fontsize=16)
plt.xlabel('Species', fontsize=12)
plt.ylabel('Population Estimate', fontsize=12)
plt.xticks(rotation=45, ha='right', fontsize=10)  # Rotate species names for better readability

# Add population values on top of the bars
for i, value in enumerate(data_clean['Cleaned Population Estimate']):
    plt.text(i, value + (value * 0.01), f'{int(value):,}', ha='center', va='bottom', fontsize=10)

# Adjust layout for better fit and display the chart
plt.tight_layout() 
plt.show() #display barchart

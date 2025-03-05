#stripping the raw data from that cleaned file (carry on from code3)

import pandas as pd

# File path of the cleaned data with raw columns 
cleaned_file = r"C:/Users/ksia/python programme/coursework/final_with_means.csv"
final_cleaned_file = r"C:/Users/ksia/python programme/coursework/stripped_final_population.csv"

#Load the cleaned dataset (from code 3 )
try:
    data = pd.read_csv(cleaned_file)
except FileNotFoundError:
    print("Error: The cleaned file was not found. Please check the file path.")
    exit()
except Exception as e:
    print(f"Error reading the file: {e}")
    exit()

#Drop raw data columns
columns_to_drop = ['Population Estimate', 'weight of the animal  (kg)', 'Life Expectancy']  # List of raw columns to remove
data = data.drop(columns=columns_to_drop, errors='ignore')  # Ignore errors if a column is missing

# Save the final dataset without raw columns
try:
    data.to_csv(final_cleaned_file, index=False)
    print(f"Stripped cleaned data has been saved to: {final_cleaned_file}")
except Exception as e:
    print(f"Error saving the file: {e}")

#View the stripped data
print("Final Data (Raw Columns Removed):")
print(data) 









import pandas as pd
import re
import numpy as np

# Input file paths
input_file = r'C:/Users/ksia/python programme/coursework/courseworkproject.csv'
refined_output_file = r"C:/Users/ksia/python programme/coursework/refined_population.csv"

# Read the dataset
try:
    data = pd.read_csv(input_file, dtype=str)  # Keep all columns as strings
except FileNotFoundError:
    print("Error: The input file was not found. Please check the file path.")
    exit()
except Exception as e:
    print(f"Error reading the file: {e}")
    exit()

# Clean column names 
data.columns = data.columns.str.strip()

#checking if the column exists
if 'Population estimate' not in data.columns:
    print("Error: 'Population estimate' column not found in the dataset. Available columns are:")
    print(data.columns.tolist())
    exit()

#Improved cleaning function
def process_population_estimate(value):
    if isinstance(value, str):
        # Remove unwanted symbol
        value = re.sub(r'~|\(.*?\)', '', value).strip()

        #1. Handle ranges : calculating the average with data that has range (e.g "10,000-25,000")
        if '-' in value:
            try:
                parts = value.split('-')
                min_val = float(parts[0].replace(',', '').strip())
                max_val = float(parts[1].replace(',', '').strip())
                return (min_val + max_val) / 2  # Average of the range
            except ValueError:
                return np.nan  # Return NaN if parsing fails

        #2. Replace cells that contains 'unknown' with NaN
        elif value.lower() == 'unknown':
            return np.nan
        
        #3. if cell contains 'less than ' values , keep it as it is 
        elif 'less than' in value.lower():
            return value
        
        #4. Also keep cells that only contain one value 
        try:
            return float(value.replace(',', '').strip()) 
        except ValueError:
            return np.nan  # Return NaN if it fails

    # Return NaN for non-string entries
    return np.nan

# Apply the function to the 'Population estimate' column (updated column name)
data['Cleaned Population Estimate'] = data['Population estimate'].apply(process_population_estimate)

#Save the cleaned data to a new file named refined output file
try:
    data.to_csv(refined_output_file, index=False)
    print(f"Refined cleaned data has been saved to: {refined_output_file}")
except Exception as e:
    print(f"Error saving the file: {e}")

#display data on shell
print("Final Cleaned Population Estimate Values:")
print(data[['Population estimate', 'Cleaned Population Estimate']])



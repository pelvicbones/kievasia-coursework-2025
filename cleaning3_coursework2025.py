#Next , i need to calculate the mean of the other numerical data column that contain ranges
#Such was weight of the animal and the life expectancy

import pandas as pd
import re
import numpy as np

#File path of the new cleaned data (from code 2 )
cleaned_file2 = r"C:/Users/ksia/python programme/coursework/final_population.csv"

#Read the new cleaned dataset
try:
    data = pd.read_csv(cleaned_file2)
except FileNotFoundError:
    print("Error: The cleaned file was not found. Please check the file path.")
    exit()
except Exception as e:
    print(f"Error reading the file: {e}")
    exit()

#Handle ranges and calculate averages
def process_ranges(value):
    if isinstance(value, str):
        # Remove unwanted characters
        value = re.sub(r'~|\(.*?\)', '', value).strip()

        # If value is a range, calculate the average
        if '-' in value:
            try:
                parts = value.split('-')
                min_val = float(parts[0].replace(',', '').strip())
                max_val = float(parts[1].replace(',', '').strip())
                return (min_val + max_val) / 2  #Return the average of the range
            except ValueError:
                return np.nan  # NaN if it fails

        # If value is a single number, leave as it is
        try:
            return float(value.replace(',', '').strip())
        except ValueError:
            return np.nan  # NaN if it fails

    #NaN for non-string values
    return np.nan

# Apply the function to columns with ranges (weight and life expectancy)
columns_to_process = ['weight of the animal  (kg)', 'Life Expectancy']  

for col in columns_to_process:
    if col in data.columns:
        data[f'Cleaned {col}'] = data[col].apply(process_ranges)

# Calculate the overall means for the both cleaned columns
for col in columns_to_process:
    cleaned_col = f'Cleaned {col}'
    if cleaned_col in data.columns:
        mean_value = data[cleaned_col].mean()
        print(f"The mean for {cleaned_col} is: {mean_value:.2f}")

#Save the updated dataset with cleaned columns
output_file = r"C:/Users/ksia/python programme/coursework/final_with_means.csv"
try:


    data.to_csv(output_file, index=False)
    print(f"Final data with cleaned columns has been saved to: {output_file}")
except Exception as e:
    print(f"Error saving the file: {e}")

#view the cleaned and updated data
print("Updated Data with Cleaned Columns and Means:")
print(data)



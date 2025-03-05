import pandas as pd
# Input file path of the cleaned version (from first code)
refined_output_file = r"C:/Users/ksia/python programme/coursework/refined_population.csv"
final_cleaned_file = r"C:/Users/ksia/python programme/coursework/final_population.csv"

#Load the cleaned file
try:
    data = pd.read_csv(refined_output_file)
except FileNotFoundError:
    print("Error: The cleaned file was not found. Please check the file path.")
    exit()
except Exception as e:
    print(f"Error reading the file: {e}")
    exit()

#Drop the raw data column
if 'Population Estimate' in data.columns:
    data = data.drop(columns=['Population Estimate'])

#Save the final cleaned file
try:
    data.to_csv(final_cleaned_file, index=False)
    print(f"Final cleaned data without the raw column has been saved to: {final_cleaned_file}")
except Exception as e:
    print(f"Error saving the file: {e}")

#View the final cleaned data
print("Final Cleaned Data (Raw Column Removed):")
print(data) 


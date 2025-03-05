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

# Make sure the necessary columns are present
if 'Conservation status' not in data.columns:
    print("Error: Required column 'Conservation status' not found in the dataset.")
    exit()

# preparing the data for visualization
# Count the number of species in each conservation status category
status_counts = data['Conservation status'].value_counts()

#Create the pie chart
plt.figure(figsize=(10, 7))
plt.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired(range(len(status_counts))))
plt.title('Proportions of species by Conservation status')
plt.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle.
plt.show()

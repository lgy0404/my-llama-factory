import os
import yaml
import pandas as pd

# Directory containing the YAML files
directory = os.path.join(os.getcwd(), 'sft_config')

# Initialize an empty list to store the extracted data
data = []

# Loop through all YAML files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.yaml'):
        # Open the YAML file and load the content
        with open(os.path.join(directory, filename), 'r') as file:
            content = file.read()
        
        # Parse the file content line by line, extracting the key-value pairs
        yaml_data = {}
        for line in content.splitlines():
            line = line.strip()  # Remove leading/trailing spaces
            # Skip lines that are comments (starting with #) or empty
            if not line or line.startswith('#'):
                continue
            
            # Only process lines that follow the "key: value" format
            if ':' in line:
                # Split the line into key and value
                key, value = line.split(':', 1)
                key = key.strip()  # Remove any leading/trailing spaces
                value = value.strip()  # Remove any leading/trailing spaces
                yaml_data[key] = value
        
        # Add the filename to the content for tracking
        yaml_data['File'] = filename
        
        # Store the data
        data.append(yaml_data)

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
output_file = 'yaml_summary.xlsx'
df.to_excel(output_file, index=False)

print(f'Summary of YAML files has been saved to {output_file}')

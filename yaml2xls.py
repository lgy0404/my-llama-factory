import os
import yaml
import pandas as pd
import json

# Directory containing the YAML files
directory = os.path.join(os.getcwd(), 'sft_config')

# Initialize an empty list to store the extracted data
data = []

# Loop through all YAML files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.yaml'):
        # Open the YAML file and load the content
        with open(os.path.join(directory, filename), 'r') as file:
            yaml_content = yaml.safe_load(file)
        
        # Extract the output_dir from the YAML content
        output_dir = yaml_content.get('output_dir', '')
        
        # Initialize a dictionary to store the YAML content and results
        yaml_data = {'File': filename}
        
        # Add all key-value pairs from the YAML file to the dictionary
        for key, value in yaml_content.items():
            yaml_data[key] = value
        
        # Check if output_dir is specified and the corresponding JSON file exists
        if output_dir:
            results_file = os.path.join(output_dir, 'all_results.json')
            if os.path.exists(results_file):
                with open(results_file, 'r') as result_file:
                    results_content = json.load(result_file)
                    yaml_data.update(results_content)
        
        # Store the data
        data.append(yaml_data)

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
output_file = 'yaml_summary.xlsx'
df.to_excel(output_file, index=False)

print(f'Summary of YAML files has been saved to {output_file}')
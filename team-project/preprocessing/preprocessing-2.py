import csv

csv.field_size_limit(400000000) 

def filter_and_create_csv(input_csv, output_csv):
    with open(input_csv, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        selected_columns = ['name', 'stars', 'forks', 'watchers', 'pullRequests',
                             'primaryLanguage', 'defaultBranchCommitCount', 'createdAt', 'license']

        with open(output_csv, 'w', newline='') as output_file:
            csv_writer = csv.DictWriter(output_file, fieldnames=selected_columns)

            csv_writer.writeheader()

            for row in csv_reader:
                try:
                    # Check if 'primaryLanguage' is not empty or NULL
                    if row['primaryLanguage']:
                        # Create a dictionary with only the selected columns
                        selected_row = {key: row[key] for key in selected_columns}
                        # Write the selected row to the new CSV file
                        csv_writer.writerow(selected_row)
                except Exception as e:
                    # Print information about the problematic row
                    print(f"Error processing row: {row}\nError: {e}")

filter_and_create_csv('output.csv', 'filtered_output.csv')

import json
import csv

def json_to_csv(json_file, csv_file):
    with open(json_file, 'r') as json_file:
        data = json.load(json_file)

    csv_data = open(csv_file, 'w')

    # Create a CSV writer
    csv_writer = csv.writer(csv_data)

    # Write the header
    header = data[0].keys() if isinstance(data, list) and len(data) > 0 else data.keys()
    csv_writer.writerow(header)

    # Write the data
    if isinstance(data, list):
        for row in data:
            csv_writer.writerow(row.values())
    else:
        csv_writer.writerow(data.values())

    csv_data.close()

json_to_csv('repo_metadata.json', 'output.csv')

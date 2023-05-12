import logging
import azure.functions as func
import csv

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Sample data
    data = [
        ['Name', 'Age', 'Gender'],
        ['John', '25', 'Male'],
        ['Jane', '30', 'Female'],
        ['Bob', '45', 'Male']
    ]

    # Create CSV file
    file_path = "example.csv"
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)

    # Return CSV file as response
    with open(file_path, mode='r') as file:
        file_content = file.read()
    headers = {
        'Content-Type': 'text/csv',
        'Content-Disposition': 'attachment; filename="example.csv"'
    }
    return func.HttpResponse(file_content, headers=headers)



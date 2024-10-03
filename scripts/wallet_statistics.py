import requests
import csv
import os
import json

def get_balance():
    url = "https://alephzero.api.subscan.io/api/scan/account/tokens"

    payload = json.dumps({
    "address": "string"
    })
    headers = {
    'User-Agent': 'Apidog/1.0.0 (https://apidog.com)',
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
        
    print(f"Request URL: {response.url}")  # Print the full request URL for debugging

        # Check if response is successful
    if response.status_code == 200:
        data = response.json()
            # Directly check if data is a list
        if isinstance(data, list) and data:  # Check if data is a non-empty list
            top_holders = data
            print("Top Holders:", top_holders)
            return top_holders
        else:
            print("No data found or data is not in expected format.")
    else:
        print("Error:", response.status_code, response.text)  # Print error message
    def get_info():
        # Define the URL for the API request
        url = "https://alephzero.api.subscan.io/api/scan/accounts/statistics"
        
        # Define the payload for the POST request
        payload = {
            "exclude_system": True,
            "type": "assets"
        }
        
        # Set headers for the request
        headers = {
            'User-Agent': 'Apidog/1.0.0 (https://apidog.com)',
            'Content-Type': 'application/json'
        }

        # Make the POST request to the API
        response = requests.post(url, json=payload, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            return response.json()['data']  # Return the data part of the response
        else:
            print(f"Failed to retrieve data: {response.status_code} - {response.text}")
            return None

def csv_save(data, csv_file_path='account_statistics.csv'):
    # Open the CSV file for writing
    with open(csv_file_path, mode='w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

        # Write header row
        csv_writer.writerow(['Name', 'Max Balance', 'Min Balance', 'Total', 'Account Count'])

        # Write data rows
        for item in data:
            row = [
                item.get('name'),
                item.get('max_balance'),
                item.get('min_balance'),
                item.get('total'),
                item.get('account_count')
            ]
            csv_writer.writerow(row)  # Write each row to the CSV

    print(f"CSV file '{csv_file_path}' has been created successfully.")

def main():
    data = get_info()  # Get information from the API
    if data:  # Proceed only if data is retrieved successfully
        csv_save(data)  # Save the data to a CSV file

if __name__ == "__main__":
    main()
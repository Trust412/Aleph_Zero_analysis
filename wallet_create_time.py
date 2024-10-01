import requests
import json
import csv
from datetime import datetime

def get_balance_history(display_address):
    """Fetches the balance history for a given display address."""
    url = "https://alephzero-testnet.api.subscan.io/api/v2/scan/transfers"

    payload = json.dumps({
        "address": display_address,
        "asset_symbol": "TZERO",
        "asset_unique_id": "TZERO",
        "order": "asc",
        "page": 0,
        "row": 1,
        "success": True
    })
    
    headers = {
        'User-Agent': 'Apidog/1.0.0 (https://apidog.com)',
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=payload)
    
    if response.status_code == 200:
        return response.json()  # Return JSON response if successful
    else:
        print(f'Error fetching balance history: {response.status_code}, {response.text}')
        return None

def convert_timestamp_to_readable(block_timestamp):
    """Converts a Unix timestamp to a human-readable format."""
    return datetime.utcfromtimestamp(block_timestamp).strftime('%Y-%m-%d %H:%M:%S')

def main():
    input_file = 'TZERO_holders.csv'  # Replace with your input CSV file name
    output_file = 'unique_users_on_the_testnet.csv'  # Output file to save results

    with open(input_file, mode='r') as infile, open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        reader = csv.DictReader(infile)
        
        # Add new column names to the output file
        fieldnames = reader.fieldnames + ['first_block_time']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        writer.writeheader()  # Write header to output file
        
        for row in reader:
            display_address = row['display_address']  # Get the display address from the CSV row
            
            # Fetch balance history for the display address
            balance_data = get_balance_history(display_address)
            
            if balance_data and balance_data['code'] == 0:
                # Extract the first block time from the response
                transfers = balance_data['data']['transfers']
                first_block_timestamp = transfers[0]['block_timestamp'] if transfers else None
                
                # Convert timestamp to readable format
                if first_block_timestamp is not None:
                    first_block_time = convert_timestamp_to_readable(first_block_timestamp)
                else:
                    first_block_time = None
                
                # Append the first block time to the row data
                row['first_block_time'] = first_block_time
            
            writer.writerow(row)  # Write updated row to output file

if __name__ == "__main__":
    main()
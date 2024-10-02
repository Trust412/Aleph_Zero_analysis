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
        "row": 100,  # Adjusted to fetch more rows if needed
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
    display_address = "5GF5Ab1REfE9CFSxFSWenuHccS4wuq6KPCP17GM4Wcvvt8hx"  # Replace with your display address
    balance_data = get_balance_history(display_address)
            
    if balance_data and balance_data['code'] == 0:
        transfers = balance_data['data']['transfers']
        
        # Open the output CSV file
        with open('balance_history.csv', mode='w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(['Transfer ID', 'From', 'To', 'Amount', 'Block Timestamp'])  # Write header
            
            for transfer in transfers:
                transfer_id = transfer['transfer_id']
                from_address = transfer['from']
                to_address = transfer['to']
                amount = transfer['amount']
                block_timestamp = convert_timestamp_to_readable(transfer['block_timestamp'])
                
                # Write each transfer's details to the CSV
                writer.writerow([transfer_id, from_address, to_address, amount, block_timestamp])
    
    print("Balance history has been written to balance_history.csv.")

if __name__ == "__main__":
    main()
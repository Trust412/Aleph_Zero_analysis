import requests
import csv

def get_token_info():
    """Function to fetch token information from the Aleph Zero API."""
    url = "https://alephzero-testnet.api.subscan.io/api/scan/token"
    headers = {
        'User-Agent': 'Apidog/1.0.0 (https://apidog.com)'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()  # Return the JSON response if successful
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None  # Return None if there's an error

def save_csv(data):
    """Function to save token information to a CSV file."""
    csv_file = 'token_info.csv'
    
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header row
        writer.writerow(['Symbol', 'Unique ID', 'Display Name', 'Asset Type', 
                         'Token Decimals', 'Price', 'Total Issuance', 
                         'Free Balance', 'Available Balance', 
                         'Locked Balance', 'Reserved Balance', 
                         'Validator Bonded', 'Nominator Bonded', 
                         'Bonded Locked Balance', 'Unbonded Locked Balance',
                         'Vesting Balance', 'Inflation'])
        
        # Extract relevant information and write to CSV
        if data and data['code'] == 0:
            token_detail = data['data']['detail']['TZERO']
            writer.writerow([
                token_detail['symbol'],
                token_detail['unique_id'],
                token_detail['display_name'],
                token_detail['asset_type'],
                token_detail['token_decimals'],
                token_detail['price'],
                token_detail['total_issuance'],
                token_detail['free_balance'],
                token_detail['available_balance'],
                token_detail['locked_balance'],
                token_detail['reserved_balance'],
                token_detail['validator_bonded'],
                token_detail['nominator_bonded'],
                token_detail['bonded_locked_balance'],
                token_detail['unbonded_locked_balance'],
                token_detail['vesting_balance'],
                token_detail['inflation']
            ])
    
    print(f"Data has been written to {csv_file}")

def main():
    """Main function to orchestrate fetching and saving token info."""
    print("Fetching token information...")
    token_data = get_token_info()
    
    print("Saving data to CSV...")
    save_csv(token_data)

if __name__ == "__main__":
    main()
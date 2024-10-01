import requests
import json
import csv

def request_data():
    """Function to make a POST request to the Aleph Zero API."""
    url = "https://alephzero-testnet.api.subscan.io/api/scan/nomination_pool/pools"
    payload = json.dumps({
        "state": "Destroying"
    })
    headers = {
        'User-Agent': 'Apidog/1.0.0 (https://apidog.com)',
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=payload)
    
    if response.status_code == 200:
        return response.json()  # Return the JSON response if successful
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None  # Return None if there's an error

def arrange_data(data):
    """Function to extract relevant information from the API response."""
    arranged_data = []
    
    if data and data['code'] == 0:
        for pool in data['data']['list']:
            pool_id = pool['pool_id']
            pool_address = pool['pool_account']['address']
            nominator_address = pool['nominator_account']['address']
            reward_address = pool['pool_reward_account']['address']
            
            # Append a tuple of extracted data
            arranged_data.append((pool_id, pool_address, nominator_address, reward_address))
    
    return arranged_data

def save_to_csv(arranged_data):
    """Function to save arranged data to a CSV file."""
    csv_file = 'pool_addresses.csv'
    
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header row
        writer.writerow(['Pool ID', 'Pool Address', 'Nominator Address', 'Reward Address'])
        
        # Write each row of arranged data
        writer.writerows(arranged_data)

    print(f"Data has been written to {csv_file}")

def main():
    """Main function to orchestrate the request, arrange, and save process."""
    print("Requesting data...")
    data = request_data()
    
    print("Arranging data...")
    arranged_data = arrange_data(data)
    
    print("Saving data to CSV...")
    save_to_csv(arranged_data)

if __name__ == "__main__":
    main()
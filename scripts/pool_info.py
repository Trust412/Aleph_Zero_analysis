import requests
import json
import csv

def get_pool_info(pool_id):
    """Fetches information about a specific nomination pool by its ID."""
    url = "https://alephzero.api.subscan.io/api/scan/nomination_pool/pool"

    payload = json.dumps({
        "pool_id": pool_id  # Use pool_id directly instead of {id}
    })
    headers = {
        'User-Agent': 'Apidog/1.0.0 (https://apidog.com)',
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=payload)
    
    if response.status_code == 200:
        return response.json()  # Return the JSON response if successful
    else:
        print(f'Error: {response.status_code}, {response.text}')  # Print error message if request failed
        return None

def csv_save(data):
    """Saves the fetched pool data into a CSV file."""
    csv_file = "nomination_pools.csv"  # Name of the CSV file to save data
    with open(csv_file, mode='a', newline='', encoding='utf-8') as file:  # Specify UTF-8 encoding
        writer = csv.writer(file)

        # Write the header row only if the file is empty
        if file.tell() == 0:  # Check if file is empty
            writer.writerow(['pool_id', 'metadata', 'state', 
                             'pool_account_address', 'pool_account_display',
                             'total_bonded', 'claimable', 'member_count'])

        if data and data['code'] == 0:
            pool_info = data['data']  # Get the pool information from the response
            writer.writerow([
                pool_info['pool_id'],
                pool_info['metadata'],
                pool_info['state'],
                pool_info['pool_account']['address'],
                pool_info['pool_account']['display'],
                pool_info['total_bonded'],
                pool_info['claimable'],
                pool_info['member_count']
            ])
    print(f'Data has been written to {csv_file}')  # Confirmation message after writing to CSV
def main():
    """Main function to fetch and save all nomination pools."""
    for pool_id in range(1, 139):  # Adjust the range based on actual pool IDs available
        print(f'Fetching information for pool ID: {pool_id}...')
        pool_data = get_pool_info(pool_id)  # Fetch pool information for each ID
        
        if pool_data:
            csv_save(pool_data)  # Save the fetched data to CSV

if __name__ == "__main__":
    main()  # Execute main function when script is run directly
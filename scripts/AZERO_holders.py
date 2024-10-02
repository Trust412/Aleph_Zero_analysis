import requests
import json
import csv

def get_AZERO_holders(page):
    url = "https://alephzero.api.subscan.io/api/scan/token/holders"

    payload = json.dumps({
        "included_zero_balance": True,
        "min_balance": 0,
        "order": "desc",
        "order_field": "balance",
        "page": page,
        "row": 100,
        "token": "AZERO",
        "unique_id": "AZERO"
    })

    response = requests.post(url, data=payload)
    if response.status_code == 200:
        return response.json()
    else: 
        print(f'Error: {response.status_code}, {response.text}')
        return None
    
def save_csv(data):
    csv_file = "AZERO_holders.csv"  # Added .csv extension
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)

        # Write the header row only if the file is empty
        if file.tell() == 0:  # Check if file is empty
            writer.writerow(['address', 'balance', 'lock', 
                             'balance_lock', 'is_EVM_contract', 
                             'display_address', 'evm_account', 
                             'registrar_info', 'count_extrinsic', 
                             'nft_amount', 'extra'])

        if data and data['code'] == 0:
            holder_detail = data['data']['list']
            for holder in holder_detail:
                writer.writerow([
                    holder['address'],
                    holder['balance'],
                    holder['lock'],
                    holder['balance_lock'],
                    holder['is_evm_contract'],
                    holder['account_display']['address'],  # Corrected to access display address
                    holder.get('evm_account', ''),  # Added default value for missing keys
                    holder.get('registrar_info', ''),
                    holder['count_extrinsic'],
                    holder['nft_amount'],
                    holder.get('extra', '')
                ])
    print(f'Data has been written to {csv_file}')

def main():
    page_number = 1
    while True:  # Loop until there are no more holders to fetch
        print(f'Fetching holders information for page {page_number}...')
        holders_data = get_AZERO_holders(page_number)
        
        if holders_data and holders_data['code'] == 0 and len(holders_data['data']['list']) > 0:
            save_csv(holders_data)
            page_number += 1  # Increment page number for the next request
        else:
            print('No more data or an error occurred.')
            break

if __name__ == "__main__":
    main()
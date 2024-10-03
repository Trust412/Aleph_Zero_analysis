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

    response = requests.post(url, data=payload, headers={'Content-Type': 'application/json'})
    if response.status_code == 200:
        return response.json()
    else: 
        print(f'Error: {response.status_code}, {response.text}')
        return None

def save_csv(data, category):
    csv_file = f"{category}_wallets.csv"  # Use category to name the CSV file
    with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
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
                    holder['account_display']['address'],  # Access display address
                    holder.get('evm_account', ''),  # Default value for missing keys
                    holder.get('registrar_info', ''),
                    holder['count_extrinsic'],
                    holder['nft_amount'],
                    holder.get('extra', '')
                ])
    print(f'Data has been written to {csv_file}')

def main():
    page_number = 1
    while True:  # Loop until there are no more holders to fetch
        holders_data = get_AZERO_holders(page_number)
        
        if holders_data and holders_data['code'] == 0 and len(holders_data['data']['list']) > 0:
            for holder in holders_data['data']['list']:
                balance = int(holder['balance'])  # Convert balance to integer for comparison
                
                if balance >=  372962573129397040:
                    print(f'Fetching whale accounts information for page {page_number}...')
                    save_csv(holders_data, 'whale')
                    page_number += 1  # Increment page number for the next request
                    break

                else:
                    if balance >= 37296257312939700:
                        print(f'Fetching dolphin accounts information for page {page_number}...')
                        save_csv(holders_data, 'dolphin')
                        page_number += 1  # Increment page number for the next request
                        break

                    else:
                        if balance >= 3729625731290:
                            print(f'Fetching fish accounts information for page {page_number}...')
                            save_csv(holders_data, 'fish')
                            page_number += 1  # Increment page number for the next request
                            break
            
        else:
            print('No more data or an error occurred.')
            break

if __name__ == "__main__":
    main()
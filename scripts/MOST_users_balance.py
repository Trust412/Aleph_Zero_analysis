import os
import requests
from dotenv import load_dotenv
import csv
from dune_client.client import DuneClient

# Load environment variables from .env file
load_dotenv()
access_key = os.getenv("DEBANK_API_KEY")
dune_api_key = os.getenv("DUNE_API_KEY")

def get_token_balances(address, start):
    url = "https://pro-openapi.debank.com/v1/user/token_list"
    headers = {
        'accept': 'application/json',
        'AccessKey': access_key
    }
    params = {'id': address, 'chain_id': 'eth', 'is_all': 'false'}
    token_balances = []

    response = requests.get(url, headers=headers, params=params)
    print(f"Request URL: {response.url}")

    if response.status_code == 200:
        data = response.json()
        if isinstance(data, list) and data:
            token_balances = data
        elif isinstance(data, dict) and 'data' in data:
            if isinstance(data['data'], list) and data['data']:
                token_balances = data['data']
        
        # Calculate USD values
        for token in token_balances:
            usd_value = calculate_usd_value(token)
            token['usd_value'] = usd_value

        print(f"Token Balances for {address}:", token_balances)
        return token_balances
    else:
        print("Error:", response.status_code, response.text)
    return token_balances

def calculate_usd_value(token):
    amount = token.get('amount', 0)
    price = token.get('price', 0)
    return (amount * price) 

def save_balances_to_csv(token_balances, address, filename='token_balances_usd.csv'):
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        try:
            writer = csv.writer(file)
            writer.writerow(['Address', 'Token Name', 'Token Symbol', 'USD Value'])
            
            for token in token_balances:
                token_name = token.get('name', 'N/A')
                token_symbol = token.get('symbol', 'N/A')
                usd_value = token.get('usd_value', 0)
                
                writer.writerow([address, token_name, token_symbol, f"${usd_value:.2f}"])
            print(f"Token balances saved to {filename}")
        except Exception as e:
            print(f"Error saving token balances to {filename}: {e}")
    return filename

def get_addresses():
    dune = DuneClient(dune_api_key)
    query_result = dune.get_latest_result(4113754)
    print(f'query_result: {query_result}')

    addresses = []
    if hasattr(query_result, 'result') and hasattr(query_result.result, 'rows'):
        for row in query_result.result.rows:
            if 'from' in row:
                addresses.append(row['from'])
    else:
        print("Unexpected structure in query result")
    
    return addresses

def main():
    try:
        user_addresses = get_addresses()
        print(f"Total addresses: {len(user_addresses)}")
        print("Extracted Addresses:")
        
        for address in user_addresses:
            print(address)
            
            try:
                token_balances = get_token_balances(address=address, start=0)
                
                if token_balances:
                    print(f"Retrieved {len(token_balances)} tokens for address {address}.")
                    filename = save_balances_to_csv(token_balances, address)
                    print(f"Saved token balances data to {filename}.")
                else:
                    print(f"No token balances found for address {address}.")
            except Exception as e:
                print(f"Error processing address {address}: {e}")
    except Exception as e:
        print(f"An error occurred in main: {e}")

if __name__ == "__main__":
    main()
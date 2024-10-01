import requests

url = "https://alephzero-testnet.api.subscan.io/api/scan/token"

payload={}
headers = {
   'User-Agent': 'Apidog/1.0.0 (https://apidog.com)'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
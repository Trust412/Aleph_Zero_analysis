import requests
import json

url = "https://alephzero-testnet.api.subscan.io/api/scan/nomination_pool/pools"

payload = json.dumps({
   "state": "Destroying"
})
headers = {
   'User-Agent': 'Apidog/1.0.0 (https://apidog.com)',
   'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
import requests

# Authentication 

TOKEN_URL = "https://api.amazon.com/auth/o2/token"

payload = {
    "grant_type": "refresh_token",
    "refresh_token": "REFRESH_TOKEN",
    "client_id": "CLIENT_ID",
    "client_secret": "CLIENT_SECRET"
}

response = requests.post(TOKEN_URL, data=payload)

if response.status_code == 200:
    access_token = response.json().get("access_token")
else:
    raise Exception("Authentication failed")

# Orders API Call

headers = {
    "Authorization": f"Bearer {access_token}",
    "x-amz-access-token": access_token
}

orders_url = "https://sellingpartnerapi-eu.amazon.com/orders/v0/orders"

params = {
    "MarketplaceIds": "A1PA6795UKMFR9",
    "CreatedAfter": "2025-01-01T00:00:00Z"
}

response = requests.get(orders_url, headers=headers, params=params)

if response.status_code == 200:
    orders_data = response.json()
else:
    print("API Error:", response.text)

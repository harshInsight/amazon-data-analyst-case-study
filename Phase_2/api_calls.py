
Phase 2: Amazon SP-API – API Calling Code
import requests
import time

BASE_URL = "https://sellingpartnerapi-na.amazon.com"

ACCESS_TOKEN = "<ACCESS_TOKEN>"      # Generated via OAuth2
LWA_CLIENT_ID = "<CLIENT_ID>"
LWA_CLIENT_SECRET = "<CLIENT_SECRET>"
REFRESH_TOKEN = "<REFRESH_TOKEN>"

HEADERS = {
    "Content-Type": "application/json",
    "x-amz-access-token": ACCESS_TOKEN
}


# GENERIC API CALL FUNCTION


def make_api_call(url, params=None):
    """
    Generic function to call Amazon SP-API
    Includes error handling & retry logic
    """
    try:
        response = requests.get(url, headers=HEADERS, params=params)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 429:
            # Rate limiting
            print("Rate limit hit. Retrying...")
            time.sleep(2)
            return make_api_call(url, params)

        else:
            print(f"Error {response.status_code}: {response.text}")
            return None

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        return None


# ORDERS API CALL

def get_orders(marketplace_id, created_after):
    """
    Fetch orders from Amazon Orders API
    """
    endpoint = f"{BASE_URL}/orders/v0/orders"

    params = {
        "MarketplaceIds": marketplace_id,
        "CreatedAfter": created_after
    }

    orders = []
    response = make_api_call(endpoint, params)

    if response and "payload" in response:
        orders.extend(response["payload"].get("Orders", []))

        # Pagination handling
        next_token = response["payload"].get("NextToken")
        while next_token:
            params = {"NextToken": next_token}
            response = make_api_call(endpoint, params)
            orders.extend(response["payload"].get("Orders", []))
            next_token = response["payload"].get("NextToken")

    return orders


# SALES API CALL


def get_sales_data(marketplace_id, start_date, end_date):
    """
    Fetch sales metrics from Amazon Sales API
    """
    endpoint = f"{BASE_URL}/sales/v1/orderMetrics"

    params = {
        "marketplaceIds": marketplace_id,
        "interval": f"{start_date}T00:00:00Z--{end_date}T23:59:59Z",
        "granularity": "Day"
    }

    response = make_api_call(endpoint, params)

    if response and "payload" in response:
        return response["payload"]

    return []


# MAIN (EXAMPLE USAGE)


if __name__ == "__main__":
    marketplace_id = "ATVPDKIKX0DER"  # US marketplace
    created_after = "2024-01-01T00:00:00Z"

    orders = get_orders(marketplace_id, created_after)
    print(f"Total Orders Fetched: {len(orders)}")

    sales = get_sales_data(
        marketplace_id,
        start_date="2024-01-01",
        end_date="2024-01-31"
    )
    print("Sales Data:", sales)


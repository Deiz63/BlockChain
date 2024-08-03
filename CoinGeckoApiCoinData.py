import requests

# Assuming the API endpoint is 'api_endpoint'
url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"

response = requests.get(url)

# If the response is successful, parse the JSON data
if response.status_code == 200:
    data = response.json()

    # Loop through each item in the data
    for item in data:
        # Extract the required fields
        coin_id = item.get('id')
        symbol = item.get('symbol')
        price = item.get('current_price')
        market_cap = item.get('market_cap')

        # Print the extracted information
        print(f"ID: {coin_id}, Symbol: {symbol}, Price: {price}, Market Cap: {market_cap}")

else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
                     
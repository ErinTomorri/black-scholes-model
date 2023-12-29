




# Replace 'YOUR_API_KEY' and 'YOUR_API_SECRET' with your actual Alpaca API key and secret
api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'
APCA_API_BASE_URL = 'https://paper-api.alpaca.markets'

# Create Alpaca API connection
#api = tradeapi.REST(api_key, api_secret, APCA_API_BASE_URL, api_version='v2')

# Example: Get options for a specific stock
symbol = 'AAPL'
options = api_key.get_options_chain(symbol, date='2023-12-29')  # Replace with a valid expiration date

# Process the options data as needed
for call_option in options['calls']:
    print(f"Strike: {call_option['strike']}, Last Price: {call_option['last']}, Volume: {call_option['volume']}")

for put_option in options['puts']:
    print(f"Strike: {put_option['strike']}, Last Price: {put_option['last']}, Volume: {put_option['volume']}")

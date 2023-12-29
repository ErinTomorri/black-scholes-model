import yfinance as yf
from scrape import wsb


def price():
    temp = wsb()
    temp1 = []
    i = 0
    while i<len(temp):
        stock_symbol = temp[i]

        # Create a Ticker object for the stock
        stock = yf.Ticker(stock_symbol)

        # Get the options data
        options_data = stock.options

        # Print the available expiration dates
        expiration_date = '2023-12-29'

        # Get options data for the chosen expiration date
        options_chain = stock.option_chain(expiration_date)

        # Print call options data
        print (options_chain.calls)
        temp1.append(options_chain.calls[['strike', 'lastPrice', 'bid', 'ask']])
        i+=1
    return temp1
print(price())
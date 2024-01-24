#https://www.quiverquant.com/wallstreetbets/
import requests
from bs4 import BeautifulSoup
import re

def wsb():
    temp = []
    # Replace 'https://example.com' with the URL of the website you want to scrape
    url = 'https://www.quiverquant.com/wallstreetbets/'
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Define a regular expression to match links with the specified pattern
        pattern = re.compile(r'../../../stock/([A-Z]+)')

        # Find all links that match the pattern
        matching_links = soup.find_all('a', href=pattern)

        # Extract and print the [A-Z]+ part of the matching links
        for link in matching_links:
            stock_symbol = pattern.search(link.get('href')).group(1)
            temp.append(stock_symbol)
        return temp
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

print (wsb())

import requests
from datetime import datetime
from bs4 import BeautifulSoup
import pandas as pd

print('Please Wait...')

# Declare start time
start_time = datetime.now()

# Specify the URL of the website you want to scrape
url = 'https://www.coingecko.com/'
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Referer": "https://www.google.com/search?q=coingecko"
}

# Make a request to the website and get the response
response = requests.get(url, headers=headers)

# Parse the HTML response into a Beautiful Soup object
soup = BeautifulSoup(response.content, 'html.parser')
end_time = datetime.now()
print('Execution duration: {}'.format(end_time - start_time))

# Save to csv using pandas
tables = []
tables.append(pd.read_html(str(soup))[0])
master_data = pd.concat(tables)
master_data = master_data.loc[:, master_data.columns[1:-1]]
master_data.to_csv('BeautifulSoup.csv', index=False)

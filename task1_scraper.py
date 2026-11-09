import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. Target a simple public website
url = "http://quotes.toscrape.com/"

print("Downloading webpage...")
response = requests.get(url)

# 2. Check if the website connected successfully
if response.status_code == 200:
    print("Webpage downloaded successfully!")
    
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all quote boxes on the page
    quote_boxes = soup.find_all('div', class_='quote')
    
    data_list = []
    
    # Loop through each quote and extract the text and author
    for box in quote_boxes:
        text = box.find('span', class_='text').get_text(strip=True)
        author = box.find('small', class_='author').get_text(strip=True)
        data_list.append({'Quote': text, 'Author': author})
        
    # 3. Save the data into a CSV file
    df = pd.DataFrame(data_list)
    df.to_csv('quotes_dataset.csv', index=False)
    print("Dataset saved successfully as 'quotes_dataset.csv'!")
else:
    print("Failed to retrieve the webpage.")
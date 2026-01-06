import requests
from bs4 import BeautifulSoup
from config import BASE_URL, USER_AGENT
from utils import can_crawl, save_to_csv

if not can_crawl(BASE_URL, USER_AGENT):
    print(f"Crawling blocked by robots.txt at {BASE_URL}")
    exit()

response = requests.get(BASE_URL, headers={'User-Agent': USER_AGENT})

if response.status_code != 200:
    print("Failed to retrieve the page")
    exit()

soup = BeautifulSoup(response.text, 'html.parser')

data = []
for quote_div in soup.find_all('div', class_='quote'):
    text = quote_div.find('span', class_='text').get_text(strip=True)
    author = quote_div.find('small', class_='author').get_text(strip=True)
    tags = [tag.get_text(strip=True) for tag in quote_div.find_all('a', class_='tag')]
    data.append({'text': text, 'author': author, 'tags': ', '.join(tags)})


csv_file = save_to_csv(data)


print(data)
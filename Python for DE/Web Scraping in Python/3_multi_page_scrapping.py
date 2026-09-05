"""
 Challenge: Scrape Books To Scrape (70 Books)

Goal:
- Visit https://books.toscrape.com/
- Scrape each book's:
  • Title 
  • Price 

You must:
- Crawl through multiple pages using the "next" button until you collect 70 books.
- Save the data to a JSON file: books_data.json
- Handle network errors gracefully.

Bonus:
- Track how many books scraped
- Print progress as you collect pages
"""


import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin

BASE_URL = "https://books.toscrape.com/"
START_PAGE = "catalogue/page-1.html"
OUTPUT_PAGE = "books_data.json"
TARGET_COUNT = 70


def scrape_page(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch page: \n {e}")
        return [], None
    
    soup = BeautifulSoup(response.text, "html.parser")
    books = []
    for article in soup.select("article.product_pod"):
        title_tag = article.select_one("h3 > a")
        title = title_tag.get("title")
        price_tag = article.select_one("p.price_color").text.strip()
        books.append({"title": title, "price": price_tag})
        
    soup_next = soup.select_one("li.next > a")
    next_page_url = urljoin(url, soup_next.get("href")) if soup_next else None
    
    return books, next_page_url

def main():
    all_books = []
    current_page = urljoin(BASE_URL, START_PAGE)
    
    while len(all_books) < TARGET_COUNT and current_page:
        print(f"Scraping page: {current_page}")
        books, next_page = scrape_page(current_page)
        all_books.extend(books)
        current_page = next_page
    
    all_books = all_books[:TARGET_COUNT]
    
    with open(OUTPUT_PAGE, "w", encoding="utf-8") as f:
        json.dump(all_books, f, indent=2)
    
    print(f"✅ Scraped {len(all_books)} books and saved to {OUTPUT_PAGE}")
    
if __name__ == "__main__":
    main()
        
        
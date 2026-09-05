"""
 Challenge: Download Cover Images Using wget

Goal:
- Scrape https://books.toscrape.com/
- Collect the first 10 books on the homepage
- Extract the title and image URL for each book
- Use the `wget` library to download and save images in a folder called 'images/'
- Use book titles (sanitized) as image filenames

Bonus:
- Add progress for each download
- Ensure folder is created if it doesn't exist
"""

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
import wget

BASE_URL = "https://books.toscrape.com/"
IMAGE_DIR = "images1"

def sanitize_filename(title):
    return re.sub(r'[^\w.-]', '', title).replace(' ', '_')

def download_image(img_url, filename):
    try:
        wget.download(img_url, filename)
        print(f"\n✅ Downloaded: {filename}")
    except Exception as e:
        print(f"\nFailed to download image: \n {e}")

def scrape_and_download_images():
    try:
        response = requests.get(BASE_URL, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch page: \n {e}")
        return
    
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.select("article.product_pod")[:10]
    
    if not os.path.exists(IMAGE_DIR):
        os.makedirs(IMAGE_DIR)
    
    for book in books:
        title_tag = book.select_one("h3 > a")
        title = title_tag.get("title")
        img_tag = book.select_one("img")
        img_url = urljoin(BASE_URL, img_tag.get("src"))
        
        sanitized_title = sanitize_filename(title)
        filename = os.path.join(IMAGE_DIR, f"{sanitized_title}.jpg")
        
        download_image(img_url, filename)
        
        
if __name__ == "__main__":
    scrape_and_download_images()
    
"""
 Challenge: Download Cover Images of First 10 Books

Goal:
- Visit https://books.toscrape.com/
- Scrape the first 10 books listed on the homepage
- For each book, extract:
  • Title
  • Image URL

Then:
- Download each image
- Save it to a local `images/` folder with the filename as the book title (sanitized)

Example:
 Title: "A Light in the Attic"
 Saved as: images/A_Light_in_the_Attic.jpg

Bonus:
- Handle invalid filename characters
- Show download progress
"""
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

BASE_URL = "https://books.toscrape.com/"
IMAGE_DIR = "images"

def sanitize_filename(title):
    return re.sub(r'[^\w.-]', '', title).replace(' ', '_')

def downlaod_image(img_url , filename):
    try:
        response = requests.get(img_url, stream=True, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to download image: \n {e}")
        return
    
    with open(filename, "wb") as f:
        for chunk in response.iter_content(1024):
            f.write(chunk)
    print(f"✅ Downloaded: {filename}")
    
    
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
        
        downlaod_image(img_url, filename)
        
        
        
if __name__ == "__main__":
    scrape_and_download_images()
    
        



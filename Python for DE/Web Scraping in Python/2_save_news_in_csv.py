"""
 Challenge: Hacker News Top Posts Scraper

Build a Python script that:
1. Fetches the HN homepage (news.ycombinator.com).
2. Extracts the top 20 post titles and URLs.
3. Saves the results into a CSV file (`hn_top20.csv`) with columns:
   - Title
   - URL
4. Handles network errors and uses a clean CSV structure.
"""
import csv
import requests
from bs4 import BeautifulSoup

HN_URL = "https://news.ycombinator.com/"
CSV_FILE = "hn_top20.csv"

def fetch_data(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch page: \n {e}")
        return []
    
    
    soup = BeautifulSoup(response.text, "html.parser")
    post_links = soup.select("span.titleline > a")
    # print(post_links)
    posts = []
    for link in post_links[:20]:
        title = link.get_text(strip=True)
        url = link.get("href")
        posts.append({"Title": title, "URL": url})
    
    return posts


def save_to_csv(posts):
    if not posts:
        print("No posts to save.")
        return
    
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Title", "URL"])
        writer.writeheader()
        writer.writerows(posts)
        
    print(f"✅ Saved {len(posts)} posts to {CSV_FILE}")
    

def main():
    print("Fetching top posts from Hacker News...")
    posts = fetch_data(HN_URL)
    print(f"Fetched {len(posts)} posts.")
    save_to_csv(posts)

if __name__ == '__main__':
    main() 
        
    
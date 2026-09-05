"""
 Challenge: Quote of the Day Image Maker

Goal:
- Scrape random quotes from https://quotes.toscrape.com/
- Extract quote text and author for the first 5 quotes
- Create an image for each quote using PIL
- Save images in 'quotes/' directory using filenames like quote_1.png, quote_2.png, etc.


"""
import os
import requests
import textwrap
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont

BASE_URL = "https://quotes.toscrape.com/"
OUTPUT_DIR = "quotes"

def scrape_quotes():
    try:
        response = requests.get(BASE_URL, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch page: \n {e}")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    quotes =soup.select("div.quote")
    quote_data = []
    
    for q in quotes[:5]:
         text = q.find("span", class_="text").text.strip("“”")
         author = q.find("small", class_ = "author").text.strip()
         quote_data.append({"text": text, "author": author})
    return quote_data

def create_image(text, author, index):
    # Create a new image
    width , height = 800, 400
    background_color = "#f8d77f"
    text_color = "#371C1C"
    
    image = Image.new("RGB", (width, height), background_color)
    
    draw = ImageDraw.Draw(image)
    
    font = ImageFont.load_default()
    author_font = ImageFont.load_default()
    
    wrapped = textwrap.fill(text, width=60)
    
    author_text = f"- {author}"
    
    y_text = 60
    x_text = 50
    
    draw.text((x_text, y_text), wrapped, font=font, fill=text_color)
    draw.text((x_text + 100, y_text + 200), author_text, font=author_font, fill=text_color)
    
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    filename = os.path.join(OUTPUT_DIR, f"quote_{index + 1}.png")
    image.save(filename)
    
    print(f"✅ Saved image: {filename}")
    

def main():
    quotes = scrape_quotes()
    
    for index, quote in enumerate(quotes):
        create_image(quote["text"], quote["author"], index)
        
if __name__ == "__main__":
    main()
    
    
    
    
        
    
"""
 Challenge: Crypto Price Tracker with Graphs

Goal:
- Fetch live prices of the top 10 cryptocurrencies using CoinGecko's free public API
- Store prices in a CSV file with timestamp
- Generate a line graph for a selected coin over time (price vs. time)
- Repeatable — user can run this multiple times to log data over time

JSON handling, API usage, CSV storage, matplotlib graphing
"""
import os
import csv
from datetime import datetime
import requests
import matplotlib.pyplot as plt


API_URL = "https://api.coingecko.com/api/v3/coins/markets"

PARAMS = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page':10,
    'page':1,
    'sparkline':False
}

CSV_FILE = 'crypto_prices.csv'

def fetch_crypto_prices():
    try:
        response = requests.get(API_URL, params=PARAMS, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch data: \n {e}")
        return []
    
    data = response.json()
    return data
    

def save_to_csv(data):
    file_exists = os.path.isfile(CSV_FILE)
    
    with open(CSV_FILE, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['timestamp', 'coin', 'price'])
        
        
        for coin in data:
            writer.writerow([datetime.now().isoformat(), coin['name'], coin['current_price']])
    print(f"✅ Saved {len(data)} records to {CSV_FILE}")



def plot_graph(coin_id):
    times = []
    prices = []
    
    if not os.path.isfile(CSV_FILE):
        print(f"No data found. Please run the script to fetch prices first.")
        return
    
    with open(CSV_FILE, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['coin'].lower() == coin_id.lower():
                times.append(datetime.fromisoformat(row['timestamp']))
                prices.append(float(row['price']))
     
    if not times:
        print(f"No data found for {coin_id}.")
        return
    
    plt.figure(figsize=(10, 5))
    plt.plot(times, prices, marker='o')
    plt.title(f"{coin_id.capitalize()} Price Over Time")
    plt.xlabel("Time")
    plt.ylabel("Price (USD)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{coin_id}_price_graph.png")
    plt.show()
    
def main():
        data = fetch_crypto_prices()
        save_to_csv(data)
        
        print("_" * 50)
        
        for coin in data:
            print(f"{coin['name']}: ${coin['current_price']}")
        print("_" * 50)
        
        coin_id = input("Enter the name of the coin to plot (e.g., bitcoin): ").strip().lower()
        if coin_id:
             plot_graph(coin_id)
if __name__ == "__main__":
    
    main()
       
    
    
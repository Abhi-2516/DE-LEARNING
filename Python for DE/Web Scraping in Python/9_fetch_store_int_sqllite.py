"""
 Challenge: Store & Search Crypto Prices in SQLite

Goal:
- Save hourly top 10 crypto prices into a local SQLite database
- Each record should include timestamp, coin ID, and price
- Allow the user to search for a coin by name and return the latest price

Teaches: SQLite handling in Python, data storage, search queries, API + DB integration
"""
import os
import csv
from datetime import datetime
import requests
import schedule
import time
import sqlite3

API_URL = "https://api.coingecko.com/api/v3/coins/markets"

PARAMS = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page':10,
    'page':1,
    'sparkline':False
}

DB_NAME = 'crypto.db'

def fetch_crypto_data():
    response = requests.get(API_URL, params=PARAMS)
    return response.json()

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS crypto_prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            coin_id TEXT,
            price REAL
        )
    ''')
    conn.commit()
    conn.close()
    
def save_to_db(data):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for coin in data:
        cursor.execute('''
            INSERT INTO crypto_prices (timestamp, coin_id, price)
            VALUES (?, ?, ?)
        ''', (timestamp, coin["id"], coin['current_price']))
    
    conn.commit()
    conn.close()
    print("✅ Data saved to SQLite database")
    
def search_coin(coin_name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT coin_id, price, timestamp
        FROM crypto_prices
        WHERE coin_id = ?
        ORDER BY timestamp DESC
        LIMIT 1
    ''', (coin_name,))
    
    result = cursor.fetchone()
    conn.close()
    
    if result:
        print(f"Latest price for {result[0]}: ${result[1]} at {result[2]}")
    else:
        print(f"No data found for coin: {coin_name}")
        

def main():
    create_table()
    
    print("1. Fetch and store crypto prices every hour")
    print("2. Search for a coin's latest price")
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        data = fetch_crypto_data()
        save_to_db(data)
    else:
        coin_name = input("Enter the coin name to search: ").strip().lower()
        search_coin(coin_name)
        
        

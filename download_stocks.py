"""
Download real stock data from Yahoo Finance
and save to your MySQL database
"""

import yfinance as yf
import pymysql
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()

# Your MySQL connection
connection = pymysql.connect(
    host=os.getenv('DB_HOST', 'localhost'),
    user=os.getenv('DB_USER', 'root'),
    password=os.getenv('DB_PASSWORD', ''),
    database=os.getenv('DB_NAME', 'finance_xai_db')
)

# Stocks to download (real companies)
stocks = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']

print("📥 Downloading stock data...")

for symbol in stocks:
    try:
        # Download from Yahoo Finance
        stock = yf.Ticker(symbol)
        hist = stock.history(period="1mo")
        
        print(f"  Got {len(hist)} days for {symbol}")
        
        # Save to MySQL
        with connection.cursor() as cursor:
            for date, row in hist.iterrows():
                sql = """
                INSERT INTO real_market_data 
                (date, symbol, open, high, low, close, volume)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(sql, (
                    date.date(),
                    symbol,
                    row['Open'],
                    row['High'],
                    row['Low'],
                    row['Close'],
                    int(row['Volume'])
                ))
        
        connection.commit()
        print(f"  ✅ Saved {symbol} to database")
        
    except Exception as e:
        print(f"  ❌ Error with {symbol}: {e}")

connection.close()
print("\n✅ Done! Check your MySQL database")
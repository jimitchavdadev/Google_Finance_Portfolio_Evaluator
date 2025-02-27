"""
fetch_data.py

This module handles fetching stock prices and foreign exchange rates from Google Finance.
It includes functions to retrieve stock price information and convert currency values.
"""

import requests as r
from bs4 import BeautifulSoup

# Define headers to mimic a real browser request to avoid blocking
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def get_fx_to_usd(currency: str) -> float:
    """
    Fetches the foreign exchange rate of a given currency to USD from Google Finance.
    
    :param currency: The three-letter currency code (e.g., 'EUR', 'CAD').
    :return: The exchange rate to USD, defaults to 1 if not found.
    """
    fx_url = f'https://www.google.com/finance/quote/{currency}-USD?hl=en'
    response = r.get(fx_url, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    fx_rate = soup.find('div', attrs={'data-last-price': True})
    if not fx_rate:
        print(f"Error: Could not fetch FX rate for {currency}")
        return 1  # Default to 1 if FX rate is not found
    
    return float(fx_rate['data-last-price'])

def get_price_information(ticker: str, exchange: str) -> dict:
    """
    Fetches the latest stock price information from Google Finance.
    
    :param ticker: The stock ticker symbol (e.g., 'MSFT', 'AAPL').
    :param exchange: The stock exchange where the stock is listed (e.g., 'NASDAQ', 'TSE').
    :return: A dictionary containing stock price details including ticker, exchange, price, currency, and USD price.
    """
    url = f'https://www.google.com/finance/quote/{ticker}:{exchange}?hl=en'
    response = r.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    price_div = soup.find('div', attrs={'data-last-price': True})
    if not price_div:
        print(f"Error: Could not fetch price for {ticker} on {exchange}")
        return {'Ticker': ticker, 'Exchange': exchange, 'Price': 0, 'Currency': 'USD', 'USD-price': 0}
    
    price = float(price_div['data-last-price'])
    currency = price_div['data-currency-code']
    
    # Convert to USD if needed
    usd_price = price
    if currency != 'USD':
        fx_rate = get_fx_to_usd(currency)
        usd_price = round(price * fx_rate, 2)
    
    return {
        'Ticker': ticker,
        'Exchange': exchange,
        'Price': price,
        'Currency': currency,
        'USD-price': usd_price
    }

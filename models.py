"""
models.py

This module defines data models for representing financial instruments such as stocks, positions, and portfolios.
It uses Python's dataclass functionality to structure and manage stock market data effectively.
"""

from dataclasses import dataclass
from typing import List
from fetch_data import get_price_information

@dataclass
class Stock:
    """
    Represents a stock with its ticker symbol, exchange, and price details.
    Automatically fetches price information upon initialization.
    """
    ticker: str
    exchange: str
    price: float = 0.0
    currency: str = 'USD'
    usd_price: float = 0.0

    def __post_init__(self):
        """
        Fetches stock price information upon object initialization.
        """
        price_info = get_price_information(self.ticker, self.exchange)
        
        if price_info['Ticker'] == self.ticker:
            self.price = price_info['Price']
            self.currency = price_info['Currency']
            self.usd_price = price_info['USD-price']

@dataclass
class Position:
    """
    Represents a stock position within a portfolio.
    Contains a reference to a Stock object and the number of shares held.
    """
    stock: Stock
    quantity: int

@dataclass
class Portfolio:
    """
    Represents a collection of stock positions.
    Provides functionality to calculate total portfolio value.
    """
    positions: List[Position]

    def get_total_value(self) -> float:
        """
        Calculates the total market value of the portfolio in USD.
        
        :return: Total portfolio value in USD.
        """
        return sum(position.quantity * position.stock.usd_price for position in self.positions)

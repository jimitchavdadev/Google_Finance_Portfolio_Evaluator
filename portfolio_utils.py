"""
portfolio_utils.py

This module provides utility functions for handling portfolio operations,
including calculating the total portfolio value and displaying portfolio summaries.
"""

from tabulate import tabulate
from models import Portfolio

def display_portfolio_summary(portfolio: Portfolio):
    """
    Displays a detailed summary of the portfolio, including stock allocations and total value.
    
    :param portfolio: An instance of the Portfolio class.
    :raises TypeError: If the provided argument is not a Portfolio instance.
    """
    if not isinstance(portfolio, Portfolio):
        raise TypeError('Please provide an instance of the Portfolio type')
    
    portfolio_value = portfolio.get_total_value()
    if portfolio_value == 0:
        print("Portfolio value is 0. Check if stocks are fetching correct prices.")
        return
    
    portfolio_data = []
    for position in sorted(portfolio.positions,
                           key=lambda x: x.quantity * x.stock.usd_price,
                           reverse=True):
        portfolio_data.append([
            position.stock.ticker,
            position.stock.exchange,
            position.quantity,
            position.stock.usd_price,
            position.quantity * position.stock.usd_price,
            position.quantity * position.stock.usd_price / portfolio_value * 100
        ])
    
    print(tabulate(portfolio_data,
                   headers=['Ticker', 'Exchange', 'Quantity', 'Price', 'Market_Value', '% Allocation'],
                   tablefmt='psql',
                   floatfmt='.2f'))
    print(f'Total portfolio value: ${portfolio_value:,.2f}')
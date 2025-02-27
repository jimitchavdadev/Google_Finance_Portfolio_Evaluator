"""
main.py

This is the entry point of the stock portfolio application. It initializes stock data,
creates a portfolio, and displays the portfolio summary.
"""

from models import Stock, Position, Portfolio
from fetch_data import get_price_information
from portfolio_utils import display_portfolio_summary

def main():
    """
    Main function to create a stock portfolio and display its summary.
    """
    try:
        # Create stock objects with real-time price fetching
        shop = Stock('SHOP', 'TSE')
        msft = Stock('MSFT', 'NASDAQ')
        nvda = Stock('NVDA', 'NASDAQ')
        bns = Stock('BNS', 'TSE')
        googl = Stock('GOOGL', 'NASDAQ')

        # Create a portfolio with stock positions
        portfolio = Portfolio([
            Position(nvda, 10),
            Position(bns, 1000),
            Position(googl, 100),
            Position(msft, 2),
            Position(shop, 30)
        ])

        # Display total portfolio value and detailed summary
        print(f"Total Portfolio Value: ${portfolio.get_total_value():,.2f}")
        display_portfolio_summary(portfolio)
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
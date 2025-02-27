# Google Finance Scraper

This project fetches stock prices and foreign exchange rates from Google Finance. It allows users to create a stock portfolio and view its total market value with detailed breakdowns.

## Features

- Retrieve real-time stock prices from Google Finance.
- Convert stock prices to USD using exchange rates.
- Create and manage a portfolio with various stock positions.
- Display a detailed summary of the portfolio, including allocations and total value.

## Installation

### Prerequisites

Ensure you have Python 3 installed on your system. You also need the required dependencies, which can be installed using:

```sh
pip install -r requirements.txt
```

### Required Libraries

- `requests`
- `beautifulsoup4`
- `tabulate`

## Usage

### Fetching Stock Prices

The `fetch_data.py` module contains functions to retrieve stock prices and foreign exchange rates from Google Finance.

Example:

```python
from fetch_data import get_price_information

stock_info = get_price_information('AAPL', 'NASDAQ')
print(stock_info)
```

### Running the Portfolio Application

To execute the portfolio application, run the following command:

```sh
python main.py
```

This script initializes a portfolio with predefined stock positions, calculates total value, and displays a detailed summary.

### Expected Output

Upon running `main.py`, you will see an output similar to:

```sh
![Portfolio Evaluation]("output.png")
```

## Project Structure

```
Google_Finance_Scraper/
│── fetch_data.py          # Fetch stock prices & FX rates
│── main.py                # Entry point for the portfolio application
│── models.py              # Defines Stock, Position, and Portfolio classes
│── portfolio_utils.py     # Utility functions for displaying portfolio data
│── requirements.txt       # List of required Python libraries
│── README.md              # Project documentation
```

## Contributing

Feel free to fork the repository and submit pull requests with improvements. If you encounter any issues, open a ticket on the repository.

## License

This project is open-source and available under the MIT License.

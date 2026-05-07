# CPE551 Final Project

## Team Members
* Rishi Konda | Email: rkonda@stevens.edu | Stevens ID: 20014780
* Dean Wise | Email: pwise@stevens.edu | Stevens ID: 20014083

## Project Description

### Project Overview
This project solves the real-world problem that people face nowadays of determining suitable investments for their portfolio. This project looks at historical data and analyzes risk and return to compare and rank assets to invest in based on performance in the past year.

### Dependencies / Libraries
* pandas: library used for loading in data, data manipulation, and dataframe handling
* yfinance: API used to retrieve historical market data for tickers
* numpy: used for mathematical operations for standard deviation and square roots
* matplotlib: used for data visualization, primarily scatter plot
* pytest: used for test cases to validate program logic
* datetime: library used to create a 1-year lookback window to retrieve historical data

### File / Module Structure
* tickers.csv: this csv file manually creates a list of ticker symbols to be analyzed
* main.ipynb: Jupyter Notebook that executes the code by initializing the screener, then ranking assets, and finalizes outputs and visualizations
* asset_models.py: Python file that contains the Asset class responsible for representing individual financial assets, calculating daily returns, annualized volatility, total return, Sharpe Ratio, and the operator overload (__lt__) for ranking assets
* screener.py: Python file that contains the Screener class, handling the composition of multiple Asset objects. Manages the API calls to Yahoo Finance, applies lambda/filter functions to remove high-risk assets, generates the CSV report, and plots the data
* test_screener.py: Python file that contains pytest functions to validate the mathematical accuracy of the volatility calculations and overall program logic

## How to Run the Program
* Ensure all project files are placed in the same folder
* Ensure that all libraries are installed
* If the necessary libraries are not installed, then run:
pip install pandas yfinance numpy matplotlib pytest
* Run the main.ipynb file to see the program output
* Run pytest test_screener.py to see PyTest test cases pass

## Main Contributions
* Rishi: worked on data handling, asset_models.py, main.ipynb
* Dean: worked on screener.py, test_screener.py


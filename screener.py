"""
Defines Screener Class and associated functions
"""

#Import all relevant libraries and classes
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from asset_models import Asset

class Screener: 
    def __init__(self, tickers, start_date, end_date):
        #Stores user inputs
        self.tickers = tickers
        self.start_date = start_date
        self.end_date = end_date
        self.assets = [] #will hold Asset objects

    def fetch_data(self):
        """
        Obtains historical price data using yfinance library
        """
        
        for ticker in self.tickers:
            try:
                #Attempts to download data from yfinance
                data = yf.download(ticker, start=self.start_date, end=self.end_date)

                #If no data is returned, skip to next part of loop
                if data.empty:
                    print(f"No data for {ticker}")
                    continue
                
                prices = data["Close"].squeeze()

                asset = Asset(ticker, prices)
                self.assets.append(asset)
            
            except Exception as e:
                print(e)

    def filter_assets(self, max_volatility):
        """
        Filters assets based on volatility and return, 
        keeping only assets that meet risk/return criteria
        """

        if max_volatility < 0: 
            raise ValueError("Volatility must not be negative")
        
        self.assets = list(filter(
            lambda a: a.volatility <= max_volatility and a.total_return > 0, 
            self.assets
        ))

    def rank_assets(self):
        """
        Sorts assets based on Sharpe Ratio
        """

        self.assets.sort(reverse = True)
"""
This is the asset_models.py file which is responsible for the Asset class
"""

import numpy as np

class Asset:
  """
  Represents data of financial asset including its symbol,
  price series, total return, and annualized volatility
  and computes a Sharpe Ratio metric
  """
  def __init__(self, ticker, price_series):
    self.ticker = str(ticker).upper()
    self.price_series = price_series
    # if the price series is not empty, it computes daily returns and the necessary metrics
    if len(self.price_series) > 1:
      # calculates the daily returns
      daily_returns = self.price_series.pct_change().dropna()
      # calculates annualized volatility
      self.volatility = np.std(daily_returns)*np.sqrt(252)*100
      # retrieves the prices to calculate total return
      start_price = self.price_series.iloc[0]
      end_price = self.price_series.iloc[-1]
      self.total_return = ((end_price-start_price)/start_price)*100
      # calculates Sharpe Ratio which represents risk-adjusted return
      if self.volatility != 0:
        self.sharpe_ratio = self.total_return/self.volatility
      else:
        self.sharpe_ratio = 0.0
    # sets the metrics to 0 if no price data is found
    else:
      self.total_return = 0.0
      self.volatility = 0.0
      self.sharpe_ratio = 0.0

  def __str__(self):
    # returns the ticker and its metrics as a string
    return f"{self.ticker}: Return = {self.total_return:.2f}%, Volatility = {self.volatility:.2f}%, Sharpe Ratio = {self.sharpe_ratio:.2f}"

  def __lt__(self, other):
    # compares assets and ranks them based on the Sharpe Ratio
    return self.sharpe_ratio < other.sharpe_ratio
import numpy as np

class Asset:
  """
  Represents financial asset and computes key metrics
  """

  def __init__(self, ticker, price_series):
    self.ticker = str(ticker).upper()
    self.price_series = price_series
    if len(self.price_series) > 1:
      daily_returns = self.price_series.pct_change().dropna()
      self.volatility = np.std(daily_returns)*np.sqrt(252)*100
      start_price = self.price_series.iloc[0]
      end_price = self.price_series.iloc[-1]
      self.total_return = ((end_price-start_price)/start_price)*100
    else:
      self.total_return = 0.0
      self.volatility = 0.0
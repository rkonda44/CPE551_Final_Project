import pandas as pd
from asset_models import Asset

def test_volatility():
    # tests to see if the volatility is greater than 0
    prices = pd.Series([100, 102, 101, 103, 104])
    asset = Asset("TEST", prices)
    assert asset.volatility > 0

def test_return():
    # tests to see if the total return is greater than 0
    prices = pd.Series([100, 110, 120, 130])
    asset = Asset("TEST", prices)
    assert asset.total_return > 0

def test_sharpe_ratio():
    # tests to see if the Sharpe Ratio logic is valid
    prices = pd.Series([100, 105, 110])
    asset = Asset("TEST", prices)
    assert asset.sharpe_ratio == (asset.total_return/asset.volatility)
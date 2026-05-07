import pandas as pd
from asset_models import Asset

def test_volatility():
    prices = pd.Series([100, 102, 101, 103, 104])
    asset = Asset("TEST", prices)
    assert asset.volatility > 0
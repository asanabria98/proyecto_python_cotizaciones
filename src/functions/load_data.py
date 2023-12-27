import pandas as pd
import numpy as np
import krakenex
from pykrakenapi import KrakenAPI
import plotly.graph_objects as go

def load_data(pair, interval):

    api = krakenex.API()
    k = KrakenAPI(api)

    # Get data
    ohlc, last = k.get_ohlc_data(pair = pair, interval = interval)

    # Reset index to get the date column
    ohlc = ohlc.reset_index()

    # clean date column
    ohlc['dtime'] = pd.to_datetime(ohlc['dtime'])

    return ohlc



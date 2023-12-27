import pandas as pd
import datetime

def data_cleaning(data, date_list):

    try:
        max_date  = date_list[1]
    except:
        max_date  = datetime.datetime.now()

    max_date = pd.to_datetime(max_date)
    min_date = pd.to_datetime(date_list[0])

    # Filtrar data

    data = data[(data['dtime'] >= min_date) & (data['dtime'] <= max_date)]


    return data

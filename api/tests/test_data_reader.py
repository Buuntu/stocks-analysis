from datetime import datetime
from django.test import Client
import pandas as pd
import json


def test_stock_data():
    client = Client()
    response = client.get('/api/stocks/NFLX')

    assert response.status_code == 200
    data = pd.read_json(response.json())
    assert len(data) > 1
    for key, value in data.iteritems():
        assert isinstance(key, datetime)


# def test_stock_data_with_dates(client):
#     response = Client.get('/stocks/NFLX', query_string=dict(
#         start_date='2019-01-01',
#         end_date='2019-02-01'
#     ))
#
#     assert response.status_code == 200
#     data = pd.read_json(response.data)
#     assert len(data.columns) > 15

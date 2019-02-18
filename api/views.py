from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import pandas_datareader.data as web
from datetime import datetime, timedelta
import json
import requests_cache

expire_after = timedelta(days=5)

session = requests_cache.CachedSession(
    cache_name='cache', backend='sqlite', expire_after=expire_after)


def stocks(request, ticker):
    try:
        start_date = request.GET.get('start_date', '')
        end_date = request.GET.get('end_date', '')
        if start_date:
            start = datetime.strptime(start_date, '%Y-%m-%d')
        else:
            start = datetime.today() - timedelta(days=10)

        if end_date:
            end = datetime.strptime(end_date, '%Y-%m-%d')
        else:
            end = datetime.today()

        data = web.DataReader(ticker, 'iex', start, end, session=session)
    except:
        abort(404)

    return HttpResponse(data.to_json(orient='index'), content_type="application/json")

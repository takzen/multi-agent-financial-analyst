# tools/financial_tools.py
import os
from langchain.tools import tool
from alpha_vantage.timeseries import TimeSeries
from newsapi import NewsApiClient

@tool
def get_stock_price(symbol: str) -> str:
    """Fetch the latest stock price for a given symbol using Alpha Vantage."""
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    ts = TimeSeries(key=api_key, output_format='pandas')
    try:
        data, _ = ts.get_quote_endpoint(symbol=symbol)
        return data.to_json()
    except Exception as e:
        return f"Error fetching stock price for {symbol}: {e}"

@tool
def get_recent_news(company_name: str) -> str:
    """Fetch recent news articles for a given company name using NewsAPI."""
    api_key = os.getenv("NEWS_API_KEY")
    newsapi = NewsApiClient(api_key=api_key)
    try:
        top_headlines = newsapi.get_everything(q=company_name, language='en', sort_by='relevancy', page_size=5)
        return str(top_headlines['articles'])
    except Exception as e:
        return f"Error fetching news for {company_name}: {e}"
import yfinance as yf
import pandas as pd
from flask import Flask, render_template, request
import plotly.graph_objects as go
import plotly.express as px

app = Flask(__name__)

# Function to get stock data from Yahoo Finance
def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    df = stock.history(period="1y")  # Get 1 year of stock data
    return df

# Function to create the stock graph using Plotly
def create_stock_graph(df):
    fig = go.Figure()

    fig.add_trace(go.Candlestick(
        x=df.index,
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close'],
        name='Stock Price'
    ))

    fig.update_layout(
        title='Stock Price Analysis',
        xaxis_title='Date',
        yaxis_title='Price (USD)',
        xaxis_rangeslider_visible=False
    )

    graph_html = fig.to_html(full_html=False)
    return graph_html

@app.route("/", methods=["GET", "POST"])
def index():
    graph_html = ""
    stock_data = None
    ticker = None
    stats = {}

    if request.method == "POST":
        ticker = request.form["ticker"]
        stock_data = get_stock_data(ticker)
        if not stock_data.empty:
            graph_html = create_stock_graph(stock_data)
            # Get basic statistics
            stats = {
                "open": stock_data['Open'].iloc[0],
                "close": stock_data['Close'].iloc[-1],
                "high": stock_data['High'].max(),
                "low": stock_data['Low'].min(),
                "volume": stock_data['Volume'].mean()
            }

    return render_template('index.html', graph_html=graph_html, stats=stats, ticker=ticker)

if __name__ == "__main__":
    app.run(debug=True)

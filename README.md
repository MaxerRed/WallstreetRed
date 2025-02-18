# WallstreetRed
An investing tool built using C++ that helps with derivative trading techniques.

#How To Use:
You will need the yfinance library to fetch historical stock data. Install it via:
#pip install yfinance

Compile the C++ code: Make sure you have a C++ compiler installed (e.g., g++).
#g++ -o derivative_calculator derivative_calculator.cpp

Run the Python Script: Now you can run the Python script, which will:

Fetch stock data using yfinance.
Call the C++ program to compute the price derivatives.
Provide investment advice based on the calculated derivatives.
Optionally, plot the stock prices and their derivatives using matplotlib.
#python stock_advisor.py

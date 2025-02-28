import subprocess
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

# Function to fetch historical stock data using Yahoo Finance
def get_stock_data(symbol, period='1mo', interval='1d'):
    stock = yf.Ticker(symbol)
    hist = stock.history(period=period, interval=interval)
    return hist['Close'].values  # We are using the 'Close' price for calculations

# Function to call the C++ program and get derivatives
def call_cpp_derivative(prices):
    # Save the prices to a temporary file to pass to C++
    with open('prices.txt', 'w') as f:
        for price in prices:
            f.write(f"{price}\n")
    
    # Call the C++ executable and capture the output
    result = subprocess.run(['./derivative_calculator'], capture_output=True, text=True)
    
    # Parse the output from the C++ program
    derivatives = list(map(float, result.stdout.strip().split()))
    
    return derivatives

# Function to provide advice based on the derivative
def generate_advice(derivatives):
    last_derivative = derivatives[-1]
    if last_derivative > 0:
        return "The stock is increasing. Consider buying!"
    elif last_derivative < 0:
        return "The stock is decreasing. Consider selling!"
    else:
        return "The stock price is stable. Hold your position."

# Main function to put everything together
def main():
    symbol = input("Enter stock symbol (e.g., AAPL): ")
    
    # Fetch stock data (e.g., last month)
    stock_prices = get_stock_data(symbol)
    
    # Get the derivatives using C++
    derivatives = call_cpp_derivative(stock_prices)
    
    # Print out the derivative values
    print("Derivative of stock prices:", derivatives)
    
    # Generate and print advice based on the derivative
    advice = generate_advice(derivatives)
    print(advice)
    
    # Optional: Plot the stock prices and derivatives
    plt.plot(stock_prices, label='Stock Price')
    plt.plot(np.arange(1, len(derivatives) + 1), derivatives, label='Price Derivative', linestyle='--')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()

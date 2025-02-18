# WallstreetRed: Derivative Trading Tool

WallstreetRed is a powerful investing tool built using C++ and Python that helps you apply derivative trading techniques to analyze stock price movements. By leveraging both numerical analysis and real-time stock data, this tool assists in making informed investment decisions based on derivatives (rate of change) of stock prices.

## Features
- Fetch historical stock data using Yahoo Finance.
- Calculate price derivatives (rate of change) using C++.
- Provide investment advice based on derivative analysis.
- Optionally, plot stock prices and their derivatives using matplotlib for better visualization.

## Prerequisites
Before you begin, ensure that you have the following installed:

- **C++ Compiler** (e.g., g++)
- **Python 3** and **pip**
- **yfinance** Python library (to fetch stock data)
  - Install using `pip install yfinance`
- **matplotlib** Python library (for plotting)
  - Install using `pip install matplotlib`

## Setup Instructions
Follow these steps to set up and run WallstreetRed:

### 1. Install Python Dependencies
To install the required Python libraries, run the following command:

```bash
pip install yfinance matplotlib
```
## Running the `derivative_calculator.cpp` and `stock_advisor.py` Files

### 2. Compile the C++ Code

To calculate the derivatives of stock prices, you will need to compile and run the `derivative_calculator.cpp` file. This will generate the rate of change for the given stock data.

#### Steps:

1. **Navigate to the directory** where the `derivative_calculator.cpp` file is located.
2. **Compile the C++ code** using the following command (assuming you're using g++):

```bash
g++ -o derivative_calculator derivative_calculator.cpp
```

#include <iostream>
#include <vector>

// Function to compute the numerical derivative of a stock price vector
std::vector<double> compute_derivative(const std::vector<double>& prices) {
    std::vector<double> derivatives;
    for (size_t i = 1; i < prices.size(); i++) {
        // Forward difference method (d/dt)
        double derivative = (prices[i] - prices[i - 1]);
        derivatives.push_back(derivative);
    }
    return derivatives;
}

int main() {

    // Calculate derivatives (rate of change)
    std::vector<double> derivatives = compute_derivative(stock_prices);

    // Output the results
    std::cout << "Price Derivatives: \n";
    for (double derivative : derivatives) {
        std::cout << derivative << " ";
    }
    std::cout << std::endl;

    return 0;
}

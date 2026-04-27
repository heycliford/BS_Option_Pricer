

# Black Scholes Option Pricing
"""
Black Scholes Assumptions:
    No dividends are paid out during the life of the option.
    Markets are random because market movements can't be predicted.
    There are no transaction costs when buying the option.
    The risk-free rate and volatility of the underlying asset are known and constant.
    The returns of the underlying asset are normally distributed.
    The option is European and can only be exercised at expiration.
"""

# IMPORTS
import numpy as np
from scipy.stats import norm

#CLASSES
class BlackScholes:
    
    def __init__(self, strike_price, stock_price, time_exp, risk_free_rate, volatility):
        self.strike_price = strike_price
        self.stock_price = stock_price
        self.time_exp = time_exp
        self.risk_free_rate = risk_free_rate
        self.volatility = volatility
        
    def call_price(self) -> float:
        
        d1 = (np.log(self.stock_price / self.strike_price) + (self.risk_free_rate + 0.5 * self.volatility**2) * self.time_exp)/ (self.volatility * np.sqrt(self.time_exp))
        d2 = d1 - (self.volatility * np.sqrt(self.time_exp))

        N_d1 = norm.cdf(d1)
        N_d2 = norm.cdf(d2)

        call_price = self.stock_price * N_d1 - self.strike_price * np.exp(-self.risk_free_rate * self.time_exp) * N_d2

        return call_price

    def __str__(self):
        return f'Option Call Price: {self.call_price()}'

def main() -> None:
    
    print(BlackScholes(100, 100, 1, 0.05, 0.5))

if __name__ == "__main__":
    main()


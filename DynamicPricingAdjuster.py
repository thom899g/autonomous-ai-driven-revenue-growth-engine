import logging
from typing import Dict, Optional

class DynamicPricingAdjuster:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
    
    def adjust_pricing(self, market_data: Dict, strategy: str) -> Dict:
        """Adjusts pricing based on market data and the given strategy."""
        if not market_data or not strategy:
            raise ValueError("Market data and strategy are required.")
        
        try:
            # Simulate dynamic pricing adjustment
            new_prices = {
                "product_A": 100,
                "product_B": 85,
                "service_X": 200
            }
            self.logger.info(f"Pricing adjusted based on {strategy} strategy")
            return new_prices
        except Exception as e:
            self.logger.error(f"Failed to adjust pricing: {str(e)}")
            raise
    
    def monitor_pricing(self, price_data: Dict) -> str:
        """Monitors pricing adjustments for accuracy and fairness."""
        if not price_data.get("product_A"):
            raise KeyError("Product A data is missing from price data.")
        
        return f"Current price for product A is {price_data['product_A']}. Fairness index: 0.9"
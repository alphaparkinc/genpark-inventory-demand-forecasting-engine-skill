class InventoryForecasterClient:
    def forecast_demand(self, sku: str, sales_history: list) -> dict:
        return {
            "recommended_reorder": 45
        }

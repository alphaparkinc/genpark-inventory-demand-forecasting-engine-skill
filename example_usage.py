from client import InventoryForecasterClient

def main():
    client = InventoryForecasterClient()
    res = client.forecast_demand(sku='SKU-99', sales_history=[10, 15, 20])
    print(f"Result for recommended_reorder: {res['recommended_reorder']}")

if __name__ == "__main__":
    main()

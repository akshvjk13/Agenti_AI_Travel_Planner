from services.data_loader import load_json_data


flights_data = load_json_data(
    "data/raw/flights.json"
)

print(f"\nTotal Flights: {len(flights_data)}")

print("\nFirst Flight Record:")
print(flights_data[0])
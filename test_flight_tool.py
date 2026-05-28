from tools.flight_tool import search_flights


results = search_flights(
    source_city="hyderabad",
    destination_city="delhi"
)

print("\nMatching Flights:\n")

for flight in results:

    print(
        f"Airline: {flight['airline']}"
    )

    print(
        f"Price: ₹{flight['price']}"
    )

    print("-" * 30)
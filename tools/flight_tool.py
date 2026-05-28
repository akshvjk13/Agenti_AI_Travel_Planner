from services.data_loader import load_json_data

def search_flights(
    source_city,
    destination_city,
    preference="cheapest"
):

    flights_data = load_json_data(
        "data/processed/cleaned_flights.json"
    )

    matching_flights = []

    source_city = source_city.strip().lower()

    destination_city = (
        destination_city.strip().lower()
    )

    for flight in flights_data:

        if (
            flight["source_city"] == source_city
            and
            flight["destination_city"]
            == destination_city
        ):

            matching_flights.append(
                flight
            )

    # Sort flights based on preference
    if preference == "cheapest":

        matching_flights = sorted(
            matching_flights,
            key=lambda flight: flight["price"]
        )

    return matching_flights
from services.data_loader import load_json_data


def search_hotels(
    city,
    preference="cheapest"
):
    """
    Search hotels based on city.
    """

    hotels_data = load_json_data(
        "data/processed/cleaned_hotels.json"
    )

    matching_hotels = []

    # Normalize user input
    city = city.strip().lower()

    for hotel in hotels_data:

        if hotel["city"] == city:

            matching_hotels.append(
                hotel
            )

    # Sort hotels based on preference
    if preference == "cheapest":

        matching_hotels = sorted(
            matching_hotels,
            key=lambda hotel:
            hotel["price_per_night"]
        )

    elif preference == "highest_rated":

        matching_hotels = sorted(
            matching_hotels,
            key=lambda hotel:
            hotel["rating"],
            reverse=True
        )

    return matching_hotels
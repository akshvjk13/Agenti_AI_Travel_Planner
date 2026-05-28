from services.data_loader import load_json_data


def search_places(  #Search places based on city and optional category.
    city,
    category=None,
    top_rated=True
):

    places_data = load_json_data(
        "data/processed/cleaned_places.json"
    )

    matching_places = []

    # Normalize user input
    city = city.strip().lower()

    if category:

        category = (
            category.strip().lower()
        )

    for place in places_data:

        # Match city
        if place["city"] != city:
            continue

        # Match category if provided
        if (
            category
            and
            place["category"] != category
        ):
            continue

        matching_places.append(
            place
        )

    # Sort by rating
    if top_rated:

        matching_places = sorted(
            matching_places,
            key=lambda place:
            place["rating"],
            reverse=True
        )

    return matching_places
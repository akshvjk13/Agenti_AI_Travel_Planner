## Flight Record Cleaner

from services.data_loader import load_json_data
import json


def normalize_text(text): #Normalize text by: converting to lowercase and removing extra spaces

    if not isinstance(text, str):
        return ""

    return text.strip().lower()


def clean_flight_record(flight): #Clean and standardize a single flight record.
    try:
        cleaned_flight = {
            "flight_id": flight.get("flight_id", "").strip(),

            "airline": normalize_text(
                flight.get("airline", "")
            ),

            "source_city": normalize_text(
                flight.get("from", "")
            ),

            "destination_city": normalize_text(
                flight.get("to", "")
            ),

            "departure_time": flight.get(
                "departure_time",
                ""
            ),

            "arrival_time": flight.get(
                "arrival_time",
                ""
            ),

            "price": float(
                flight.get("price", 0)
            )
        }

        # Validation check
        if (
            cleaned_flight["source_city"] == ""
            or cleaned_flight["destination_city"] == ""
            or cleaned_flight["price"] <= 0
        ):
            return None
        return cleaned_flight
    except Exception as error:
        print(f"Error cleaning flight record: {error}")
        return None
    
def clean_flights_data(): #Load, clean, and save flights dataset.
    flights_data = load_json_data(
        "data/raw/flights.json"
    )
    cleaned_flights = []
    for flight in flights_data:
        cleaned_record = clean_flight_record(
            flight
        )
        if cleaned_record:
            cleaned_flights.append(
                cleaned_record
            )
    # Save cleaned dataset
    with open(
        "data/processed/cleaned_flights.json",
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            cleaned_flights,
            file,
            indent=4
        )
    print(
        f"Successfully cleaned "
        f"{len(cleaned_flights)} flights."
    )

## Hotel Record Cleaner

def clean_hotel_record(hotel):# Clean and standardize a single hotel record.
    try:
        cleaned_hotel = {

            "hotel_id": hotel.get(
                "hotel_id",
                ""
            ).strip(),

            "hotel_name": normalize_text(
                hotel.get("name", "")
            ),

            "city": normalize_text(
                hotel.get("city", "")
            ),

            "rating": float(
                hotel.get("stars", 0)
            ),

            "price_per_night": float(
                hotel.get("price_per_night", 0)
            ),

            "amenities": hotel.get(
                "amenities",
                []
            )
        }

        # Validation
        if (
            cleaned_hotel["city"] == ""
            or cleaned_hotel["price_per_night"] <= 0
        ):
            return None

        return cleaned_hotel

    except Exception as error:
        print(f"Error cleaning hotel record: {error}")
        return None
    
# Clean Entire Hotels Dataset
def clean_hotels_data():
    """
    Load, clean, and save hotels dataset.
    """

    hotels_data = load_json_data(
        "data/raw/hotels.json"
    )

    cleaned_hotels = []

    for hotel in hotels_data:

        cleaned_record = clean_hotel_record(
            hotel
        )

        if cleaned_record:
            cleaned_hotels.append(
                cleaned_record
            )

    with open(
        "data/processed/cleaned_hotels.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            cleaned_hotels,
            file,
            indent=4
        )

    print(
        f"Successfully cleaned "
        f"{len(cleaned_hotels)} hotels."
    )

# CLEAN PLACES

def clean_place_record(place): #  Clean and standardize a single place record.
    try:
        cleaned_place = {

            "place_id": place.get(
                "place_id",
                ""
            ).strip(),

            "place_name": normalize_text(
                place.get("name", "")
            ),

            "city": normalize_text(
                place.get("city", "")
            ),

            "category": normalize_text(
                place.get("type", "")
            ),

            "rating": float(
                place.get("rating", 0)
            )
        }

        # Validation
        if (
            cleaned_place["city"] == ""
            or cleaned_place["place_name"] == ""
        ):
            return None

        return cleaned_place

    except Exception as error:
        print(f"Error cleaning place record: {error}")
        return None

# Clean Entire Places Dataset

def clean_places_data(): # Load, clean, and save places dataset.

    places_data = load_json_data(
        "data/raw/places.json"
    )

    cleaned_places = []

    for place in places_data:

        cleaned_record = clean_place_record(
            place
        )

        if cleaned_record:
            cleaned_places.append(
                cleaned_record
            )

    with open(
        "data/processed/cleaned_places.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            cleaned_places,
            file,
            indent=4
        )

    print(
        f"Successfully cleaned "
        f"{len(cleaned_places)} places."
    )

if __name__ == "__main__":

    clean_flights_data()

    clean_hotels_data()

    clean_places_data()

    print(
        f"Data cleaning completed for flights, hotels, and places datasets."
    )
from tools.hotel_tool import search_hotels


results = search_hotels(
    city="delhi",
    preference="highest_rated"
)

print("\nMatching Hotels:\n")

for hotel in results:

    print(
        f"Hotel: {hotel['hotel_name']}"
    )

    print(
        f"Rating: {hotel['rating']}"
    )

    print(
        f"Price Per Night: "
        f"₹{hotel['price_per_night']}"
    )

    print("-" * 30)
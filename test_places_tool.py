from tools.places_tool import search_places


results = search_places(
    city="delhi",
    category="museum"
)

print("\nRecommended Places:\n")

for place in results:

    print(
        f"Place: {place['place_name']}"
    )

    print(
        f"Category: {place['category']}"
    )

    print(
        f"Rating: {place['rating']}"
    )

    print("-" * 30)
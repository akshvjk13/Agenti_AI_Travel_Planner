import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.dirname(__file__)
    )
)

import streamlit as st

from tools.flight_tool import search_flights
from tools.hotel_tool import search_hotels
from tools.places_tool import search_places
from tools.budget_tool import estimate_budget
from tools.weather_tool import get_weather_forecast

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# PAGE TITLE
st.title("✈️ AI Travel Planner Assistant")

# USER INPUTS
source_city = st.text_input(
    "Source City"
)

destination_city = st.text_input(
    "Destination City"
)

departure_date = st.date_input(
    "Departure Date"
)

return_date = st.date_input(
    "Return Date"
)

days = (
    return_date - departure_date
).days

# BUTTON
if st.button("Generate Travel Plan"):

    # VALIDATION
    if not source_city or not destination_city or not days:

        st.warning(
            "Please fill all fields."
        )

        st.stop()

    # VALIDATE DAYS
    if days <= 0:

        st.error(
            "Return date must be after departure date."
        )

        st.stop()

    # LOADING SPINNER
    with st.spinner("Generating AI Travel Plan..."):

        # FLIGHTS
        flights = search_flights(
            source_city=source_city.lower(),
            destination_city=destination_city.lower(),
            preference="cheapest"
        )
        for flight in flights:

            flight["departure_time"] = (
                str(departure_date) + " 09:00 AM"
            )

            flight["arrival_time"] = (
                str(return_date) + " 11:30 AM"
            )

        # HOTELS
        hotels = search_hotels(
            city=destination_city.lower()
        )

        # PLACES
        places = search_places(
            city=destination_city.lower()
        )

        # WEATHER
        weather = get_weather_forecast(
            city=destination_city.lower()
        )

        # WEATHER SUMMARY
        weather_summary = ""

        if weather and "daily" in weather:

            max_temp = max(
                weather["daily"]["temperature_2m_max"]
            )

            min_temp = min(
                weather["daily"]["temperature_2m_min"]
            )

            weather_summary = (
                f"{destination_city.title()} "
                f"will have temperatures ranging "
                f"from {min_temp}°C to {max_temp}°C "
                f"during the trip."
            )

        # BUDGET
        budget = estimate_budget(
            flight_cost=flights[0]["price"],
            hotel_price_per_night=hotels[0]["price_per_night"],
            number_of_days=days
        )

        # PROMPT
        prompt = f"""
        Create a professional travel itinerary.

        Source City:
        {source_city}

        Destination:
        {destination_city}

        Departure Date:
        {departure_date}

        Return Date:
        {return_date}

        Trip Duration:
        {days} days

        Flights:
        {flights[:3]}

        Hotels:
        {hotels[:3]}

        Tourist Places:
        {places[:5]}

        Weather:
        {weather_summary}

        Budget:
        ₹{budget}

        Generate a clean and professional travel plan with:

        1. Trip Summary
        2. Recommended Flight
        3. Hotel Recommendation
        4. Places to Visit
        5. Weather Information
        6. Day-wise Itinerary
        7. Budget Breakdown
        8. Travel Tips

        IMPORTANT:
        - Put Weather in a separate paragraph.
        - Use proper markdown formatting.
        - Use bullet points where necessary.
        - Keep itinerary realistic.
        - Do not make up information. Use only the provided data.
        -Use the user-selected travel dates instead of flight dataset dates.
        -Do not mention outdated years like 2025.
        """

        # AI RESPONSE
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        # DISPLAY OUTPUT
        st.subheader("Generated Travel Plan")

        st.markdown(
            response.choices[0].message.content
        )
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from dotenv import load_dotenv

from groq import Groq

from tools.flight_tool import (
    search_flights
)

from tools.hotel_tool import (
    search_hotels
)

from tools.places_tool import (
    search_places
)

from tools.budget_tool import (
    estimate_budget
)

from tools.weather_tool import (
    get_weather_forecast
)

# LOAD ENV VARIABLES
load_dotenv()

client = Groq(
    api_key=os.getenv(
        "GROQ_API_KEY"
    )
)

# USER 
user_query = """
Plan a 3-day trip from Hyderabad to Delhi
with hotel, attractions, weather,
and total budget.
"""

# TOOL EXECUTION
flights = search_flights(
    source_city="hyderabad",
    destination_city="delhi",
    preference="cheapest"
)

hotels = search_hotels(
    city="delhi"
)

places = search_places(
    city="delhi"
)

weather = get_weather_forecast(
    city="delhi"
)

budget = estimate_budget(
    flight_cost=flights[0]["price"],
    hotel_price_per_night=hotels[0]["price_per_night"],
    number_of_days=3
)

# PROMPT FOR LLM
prompt = f"""
You are an AI Travel Planner.

User Query:
{user_query}

Flights:
{flights[:3]}

Hotels:
{hotels[:3]}

Places:
{places[:5]}

Weather:
{weather}

Estimated Budget:
₹{budget}

Create:
1. Trip Summary
2. Best Flight
3. Recommended Hotel
4. Day-wise itinerary
5. Budget breakdown
6. Travel tips
"""

# LLM CALL
response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.7
)

# FINAL OUTPUT
print("\nTRAVEL PLAN:\n")

print(
    response.choices[0].message.content
)
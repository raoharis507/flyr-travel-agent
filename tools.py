import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file!")

client = Groq(api_key=api_key)

def ask_groq(prompt: str) -> str:
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1024
    )
    return response.choices[0].message.content

def search_flights(origin: str, destination: str, date: str) -> str:
    prompt = f"""You are a flight search expert. Find realistic flight options from {origin} to {destination} on {date}.
    Return exactly 3 flight options with:
    - Airline name and flight number
    - Departure and arrival times
    - Flight duration
    - Price in USD
    - One reason why its recommended
    Format it cleanly and professionally."""
    return ask_groq(prompt)

def search_hotels(destination: str, checkin: str, days: int) -> str:
    prompt = f"""You are a hotel expert. Find realistic hotel options in {destination} for {days} nights from {checkin}.
    Return exactly 3 hotel options with:
    - Hotel name and star rating
    - Price per night in USD
    - Key amenities (3-4 points)
    - Location description
    - Why its recommended
    Format it cleanly and professionally."""
    return ask_groq(prompt)

def get_weather(destination: str, date: str, days: int) -> str:
    prompt = f"""You are a weather expert. Provide a realistic weather forecast for {destination} starting {date} for {days} days.
    Include:
    - Daily temperature highs and lows in Celsius and Fahrenheit
    - Weather conditions for each day
    - What to pack (5 items)
    - Best times to go outdoors
    Format it cleanly and professionally."""
    return ask_groq(prompt)

def calculate_budget(origin: str, destination: str, days: int) -> str:
    prompt = f"""You are a travel budget expert. Calculate a realistic budget for a {days}-day trip from {origin} to {destination}.
    Include:
    - Flight cost estimate (round trip)
    - Hotel cost (budget, mid-range, luxury per night)
    - Daily food budget
    - Local transport per day
    - Activities and entrance fees
    - Total estimated cost for budget, mid-range and luxury traveler
    Format with clear sections and USD prices."""
    return ask_groq(prompt)

def create_itinerary(destination: str, days: int, interests: str) -> str:
    prompt = f"""You are an expert travel designer. Create a detailed {days}-day itinerary for {destination}
    for someone interested in: {interests}.
    For each day include:
    - Morning activity with location name
    - Lunch restaurant recommendation
    - Afternoon activity with location name
    - Evening dinner and activity recommendation
    - Estimated cost for the day in USD
    Make it exciting, realistic and personalized."""
    return ask_groq(prompt)

def create_summary(origin: str, destination: str, date: str, days: int,
                   flights: str, hotels: str, weather: str,
                   budget: str, itinerary: str) -> str:
    prompt = f"""You are a professional travel consultant. Create a warm executive summary for this trip:
    - From: {origin}
    - To: {destination}
    - Date: {date}
    - Duration: {days} days

    Based on these findings:
    FLIGHTS: {flights[:400]}
    HOTELS: {hotels[:400]}
    WEATHER: {weather[:400]}
    BUDGET: {budget[:400]}

    Write a professional 3-paragraph summary highlighting:
    1. Best flight and hotel choice
    2. Weather and what to pack
    3. Top tip for this destination
    Keep it warm, helpful and exciting."""
    return ask_groq(prompt)
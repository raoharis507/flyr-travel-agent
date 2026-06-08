from crewai import Task
from tools import (
    search_flights,
    search_hotels,
    get_weather,
    calculate_budget,
    create_itinerary
)

def create_tasks(agents, trip_details):
    origin = trip_details["origin"]
    destination = trip_details["destination"]
    date = trip_details["date"]
    days = trip_details["days"]
    interests = trip_details["interests"]

    flight_task = Task(
        description=f"""Search for the best flights from {origin} to {destination} 
        on {date}. Analyze all options and recommend the best one based on 
        price and timing.""",
        expected_output="A detailed flight recommendation with price, timing and airline",
        agent=agents["flight_agent"],
        tools=[search_flights]
    )

    hotel_task = Task(
        description=f"""Search for the best hotels in {destination} for {days} nights 
        starting {date}. Consider comfort, location and value for money.""",
        expected_output="A hotel recommendation with price per night, stars and amenities",
        agent=agents["hotel_agent"],
        tools=[search_hotels]
    )

    weather_task = Task(
        description=f"""Get the weather forecast for {destination} during the travel 
        dates starting {date} for {days} days. Provide packing recommendations.""",
        expected_output="A weather forecast with temperature, conditions and packing tips",
        agent=agents["weather_agent"],
        tools=[get_weather]
    )

    budget_task = Task(
        description=f"""Calculate the complete budget for a {days} day trip to 
        {destination}. Include flights, hotels, food and local transport costs.""",
        expected_output="A complete budget breakdown with total cost estimation",
        agent=agents["budget_agent"],
        tools=[calculate_budget]
    )

    itinerary_task = Task(
        description=f"""Create a detailed {days}-day itinerary for {destination} 
        based on these interests: {interests}. Make it exciting and well organized.""",
        expected_output="A day-by-day itinerary with activities, timings and tips",
        agent=agents["itinerary_agent"],
        tools=[create_itinerary]
    )

    summary_task = Task(
        description=f"""Review all the information gathered by the other agents about 
        the trip to {destination}. Compile everything into one final comprehensive 
        travel plan including flights, hotels, weather, budget and itinerary.""",
        expected_output="A complete travel plan summary combining all agent findings",
        agent=agents["orchestrator"],
        context=[flight_task, hotel_task, weather_task, budget_task, itinerary_task]
    )

    return [flight_task, hotel_task, weather_task, budget_task, itinerary_task, summary_task]
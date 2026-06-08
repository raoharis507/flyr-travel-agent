import os
from dotenv import load_dotenv
from tools import (
    search_flights,
    search_hotels,
    get_weather,
    calculate_budget,
    create_itinerary,
    create_summary
)

load_dotenv()

class FlightAgent:
    def __init__(self):
        self.name = "Flight Agent"
        self.icon = "✈️"
        self.role = "Flight Search Specialist"

    def run(self, origin, destination, date):
        print(f"🔍 {self.name} searching flights...")
        result = search_flights(origin, destination, date)
        return result

class HotelAgent:
    def __init__(self):
        self.name = "Hotel Agent"
        self.icon = "🏨"
        self.role = "Accommodation Specialist"

    def run(self, destination, checkin, days):
        print(f"🔍 {self.name} searching hotels...")
        result = search_hotels(destination, checkin, days)
        return result

class WeatherAgent:
    def __init__(self):
        self.name = "Weather Agent"
        self.icon = "🌤️"
        self.role = "Weather Analyst"

    def run(self, destination, date, days):
        print(f"🔍 {self.name} checking weather...")
        result = get_weather(destination, date, days)
        return result

class BudgetAgent:
    def __init__(self):
        self.name = "Budget Agent"
        self.icon = "💰"
        self.role = "Financial Planner"

    def run(self, origin, destination, days):
        print(f"🔍 {self.name} calculating budget...")
        result = calculate_budget(origin, destination, days)
        return result

class ItineraryAgent:
    def __init__(self):
        self.name = "Itinerary Agent"
        self.icon = "📅"
        self.role = "Trip Designer"

    def run(self, destination, days, interests):
        print(f"🔍 {self.name} designing itinerary...")
        result = create_itinerary(destination, days, interests)
        return result

class OrchestratorAgent:
    def __init__(self):
        self.name = "Orchestrator Agent"
        self.icon = "🎯"
        self.role = "Master Coordinator"

    def run(self, origin, destination, date, days,
            flights, hotels, weather, budget, itinerary):
        print(f"🔍 {self.name} compiling final plan...")
        result = create_summary(
            origin, destination, date, days,
            flights, hotels, weather, budget, itinerary
        )
        return result


class FlyRCrew:
    def __init__(self):
        self.flight_agent = FlightAgent()
        self.hotel_agent = HotelAgent()
        self.weather_agent = WeatherAgent()
        self.budget_agent = BudgetAgent()
        self.itinerary_agent = ItineraryAgent()
        self.orchestrator = OrchestratorAgent()

    def run(self, trip_details, progress_callback=None):
        origin = trip_details["origin"]
        destination = trip_details["destination"]
        date = trip_details["date"]
        days = trip_details["days"]
        interests = trip_details["interests"]

        results = {}

        # Step 1 - Flight Agent
        if progress_callback:
            progress_callback(1, "✈️ Flight Agent searching for best flights...")
        results["flights"] = self.flight_agent.run(origin, destination, date)

        # Step 2 - Hotel Agent
        if progress_callback:
            progress_callback(2, "🏨 Hotel Agent finding accommodations...")
        results["hotels"] = self.hotel_agent.run(destination, date, days)

        # Step 3 - Weather Agent
        if progress_callback:
            progress_callback(3, "🌤️ Weather Agent checking forecasts...")
        results["weather"] = self.weather_agent.run(destination, date, days)

        # Step 4 - Budget Agent
        if progress_callback:
            progress_callback(4, "💰 Budget Agent calculating costs...")
        results["budget"] = self.budget_agent.run(origin, destination, days)

        # Step 5 - Itinerary Agent
        if progress_callback:
            progress_callback(5, "📅 Itinerary Agent designing your trip...")
        results["itinerary"] = self.itinerary_agent.run(destination, days, interests)

        # Step 6 - Orchestrator
        if progress_callback:
            progress_callback(6, "🎯 Orchestrator compiling your final plan...")
        results["summary"] = self.orchestrator.run(
            origin, destination, date, days,
            results["flights"], results["hotels"],
            results["weather"], results["budget"],
            results["itinerary"]
        )

        return results
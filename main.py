import os
from dotenv import load_dotenv
from agents import FlyRCrew

load_dotenv()

def run_travel_planner(trip_details, progress_callback=None):
    print("\n🛫 FlyR AI Travel System Starting...")
    print(f"📍 Destination: {trip_details['destination']}")
    print("=" * 50)

    crew = FlyRCrew()
    results = crew.run(trip_details, progress_callback)

    print("\n✅ All agents completed successfully!")
    return results


if __name__ == "__main__":
    trip_details = {
        "origin": "Lahore",
        "destination": "Paris",
        "date": "2026-07-15",
        "days": 5,
        "interests": "art, museums, food, history"
    }

    def simple_progress(step, message):
        print(f"Step {step}/6: {message}")

    results = run_travel_planner(trip_details, simple_progress)

    print("\n" + "=" * 50)
    print("✅ FLIGHTS:")
    print(results["flights"])
    print("\n✅ HOTELS:")
    print(results["hotels"])
    print("\n✅ WEATHER:")
    print(results["weather"])
    print("\n✅ BUDGET:")
    print(results["budget"])
    print("\n✅ ITINERARY:")
    print(results["itinerary"])
    print("\n✅ SUMMARY:")
    print(results["summary"])
    
## 🎬 Video Presentation
👉 [Watch Project Demo Video](https://drive.google.com/file/d/1zjx88JB-UZd1uoVADFlS7UjbjvHwMq8O/view?usp=drive_link)

---

# 🛫 FlyR — AI Multi-Agent Travel Planner

## Problem Domain
Travel planning is a complex task requiring simultaneous evaluation of flights, hotels, weather, budget and itineraries. FlyR solves this using 6 specialised AI agents that each handle one domain, coordinated by a master Orchestrator agent that compiles everything into one comprehensive travel plan.

---

## Architecture

FlyR uses a hierarchical multi-agent architecture:
User Input (Origin, Destination, Date, Interests)

│

▼

┌─────────────────┐

│  Orchestrator   │

│     Agent       │

└────────┬────────┘

│

┌────────────┼────────────┐

│            │            │

▼            ▼            ▼

Flight        Hotel        Weather

Agent         Agent         Agent

│            │            │

▼            ▼            ▼

Budget                  Itinerary

Agent                     Agent

│                        │

└──────────┬─────────────┘

▼

Final Travel Plan

### Agent Roles

| Agent | Role |
|---|---|
| Orchestrator Agent | Coordinates all agents and compiles the final plan |
| Flight Agent | Searches best flights by price and schedule |
| Hotel Agent | Finds hotels matching budget and preferences |
| Weather Agent | Provides forecasts and packing recommendations |
| Budget Agent | Calculates complete trip cost breakdown |
| Itinerary Agent | Creates personalised day-by-day travel plan |

### Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.11 | Core programming language |
| Groq API (LLaMA 3.3 70B) | AI brain for all agents |
| Streamlit | Web UI framework |
| python-dotenv | Environment variable management |

---

## Instructions to Start the Project

### 1. Clone the repository
```bash
git clone https://github.com/raoharis507/flyr-travel-agent.git
cd flyr-travel-agent
```

### 2. Create virtual environment
```bash
python3.11 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Set up API key
Create a `.env` file:
GROQ_API_KEY=your_groq_api_key_here
Get your free key at: https://console.groq.com/

### 5. Run the app
```bash
streamlit run app.py
```

### 6. Open in browser
http://localhost:8501

---

## How to Use

1. Enter your **departure city** in Flying From
2. Enter your **destination city**
3. Select your **travel date**
4. Choose **number of days**
5. Enter your **interests** (e.g. art, food, history)
6. Click **Launch AI Agents**
7. Watch all 6 agents work in real time
8. Get your complete AI travel plan!

---

## Project Structure
flyr-travel-agent/

├── app.py            # Streamlit web UI

├── main.py           # Entry point

├── agents.py         # All 6 agent definitions

├── tasks.py          # Task definitions

├── tools.py          # AI functions using Groq API

├── .env              # API key (not included)

├── requirements.txt  # Dependencies

└── README.md         # This file

---

## AI Tool Declaration
This project was developed with assistance from Claude AI (Anthropic) for code structure and UI design. All code has been reviewed, tested and understood by the student. Tools used: Claude AI. Verification: manual testing across multiple trip configurations and independent debugging.

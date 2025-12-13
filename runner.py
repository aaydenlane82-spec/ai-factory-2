import json, os, random
from datetime import datetime

ideas = ["AI health tracker", "Budget app", "Study planner", "Habit tracker", "Fitness coach", "Meal planner", "Sleep optimizer", "Focus timer"]

state = json.load(open("state.json")) if os.path.exists("state.json") else {"runs": 0}
state["runs"] += 1
state["last_run"] = datetime.utcnow().isoformat()

print(f"🤖 Run #{state['runs']}: {random.choice(ideas)}")
json.dump(state, open("state.json", "w"))

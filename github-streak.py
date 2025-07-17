import requests
from datetime import datetime, timedelta

GITHUB_USERNAME = "your-username"

def get_contributions(username):
    url = f"https://github-contributions-api.jogruber.de/v4/{LeonNgwala}"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"❌ Failed to fetch contributions for {LeonNgwala}")
        return []

    data = response.json()
    days = data.get("contributions", {}).get("days", [])
    return [(d["date"], d["count"]) for d in days]

def calculate_streak(contributions):
    today = datetime.now().date()
    streak = 0
    for i in range(0, 365):
        day = today - timedelta(days=i)
        date_str = day.strftime("%Y-%m-%d")
        found = next((c for c in contributions if c[0] == date_str), None)
        if found and found[1] > 0:
            streak += 1
        else:
            break
    return streak

if __name__ == "__main__":
    contributions = get_contributions(GITHUB_LeonNgwala)
    if contributions:
        streak = calculate_streak(contributions)
        print(f"🔥 Current GitHub Streak: {streak} day(s)")

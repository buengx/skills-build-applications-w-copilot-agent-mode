import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client['octofit_db']

# Insert test users
db.users.insert_many([
    {"email": "alice@example.com", "name": "Alice", "password": "alicepass"},
    {"email": "bob@example.com", "name": "Bob", "password": "bobpass"}
])

# Insert test teams
db.teams.insert_many([
    {"name": "Team Alpha", "members": ["alice@example.com"]},
    {"name": "Team Beta", "members": ["bob@example.com"]}
])

# Insert test activities
db.activity.insert_many([
    {"user": "alice@example.com", "type": "run", "duration": 30, "date": "2025-05-13T08:00:00Z"},
    {"user": "bob@example.com", "type": "walk", "duration": 45, "date": "2025-05-13T09:00:00Z"}
])

# Insert test workouts
db.workouts.insert_many([
    {"user": "alice@example.com", "name": "Pushups", "description": "20 pushups", "date": "2025-05-13T08:10:00Z"},
    {"user": "bob@example.com", "name": "Situps", "description": "30 situps", "date": "2025-05-13T09:10:00Z"}
])

# Insert test leaderboard
db.leaderboard.insert_many([
    {"team": "Team Alpha", "points": 100},
    {"team": "Team Beta", "points": 80}
])

print("Test data inserted into octofit_db.")

from lib.models import SessionLocal, Startup, Pitch, Investor
from datetime import datetime

# get a new database session
def get_session():
    return SessionLocal()

# calculate the average interest
def calculate_average_interest(session, startup_id):
    pitches = Pitch.get_all_for_startup(session, startup_id)
    if not pitches:
        return 0
    return sum(p.interest_rating for p in pitches) / len(pitches)

# get top investors
def get_most_interested_investors(session, startup_id):
    pitches = Pitch.get_all_for_startup(session, startup_id)
    if not pitches:
        return []
    return sorted(pitches, key=lambda p: p.interest_rating, reverse=True)[:3]
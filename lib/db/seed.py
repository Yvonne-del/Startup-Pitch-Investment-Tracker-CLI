from lib.models.startup import Startup
from lib.models.pitch import Pitch
from lib.models.investor import Investor

from datetime import date
import random

def seed():
    session = SessionLocal()

    # Clear old data (optional)
    session.query(Pitch).delete()
    session.query(Investor).delete()
    session.query(Startup).delete()
    session.commit()

    # Seed startups
    startups = [
        Startup.create(session, "AlphaTech", "AI-based solutions", "Series A"),
        Startup.create(session, "BetaHealth", "Health tracking app", "Seed"),
        Startup.create(session, "GammaFinance", "Fintech platform", "Pre-Seed"),
    ]

    # Seed investors
    investors = [
        Investor.create(session, "Alice Johnson", "VentureOne", "Tech"),
        Investor.create(session, "Bob Smith", "Capital Group", "Health"),
        Investor.create(session, "Carol Lee", "Finance Ventures", "Finance"),
    ]

    # Seed pitches with random interest ratings and feedback
    feedbacks = ["Very interested", "Needs more info", "Not convinced", "Looking forward", "Follow-up needed"]
    for _ in range(10):
        s = random.choice(startups)
        i = random.choice(investors)
        rating = random.randint(0, 5)
        fb = random.choice(feedbacks)
        Pitch.create(session, s.id, i.id, date.today(), fb, rating)

    print("Database seeded with sample data.")
    session.close()

if __name__ == "__main__":
    seed()

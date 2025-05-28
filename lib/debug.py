from lib.models.startup import Startup
from lib.models.pitch import Pitch
from lib.models.investor import Investor

from datetime import date

def run_debug():
    session = SessionLocal()

    print("=== Debug: Create a startup ===")
    s = Startup.create(session, "Debug Startup", "Testing startup creation", "Seed")
    print(f"Created Startup: ID={s.id}, Name={s.name}")

    print("=== Debug: Create an investor ===")
    i = Investor.create(session, "Debug Investor", "Debug Firm", "Tech")
    print(f"Created Investor: ID={i.id}, Name={i.name}")

    print("=== Debug: Create a pitch ===")
    p = Pitch.create(session, s.id, i.id, date.today(), "Looks promising", 4)
    print(f"Created Pitch: ID={p.id}, Startup={p.startup.name}, Investor={p.investor.name}, Rating={p.interest_rating}")

    print("=== Debug: Fetch all startups ===")
    all_startups = Startup.get_all(session)
    for startup in all_startups:
        print(f"- {startup.id}: {startup.name} ({startup.funding_stage})")

    print("=== Debug: Fetch all investors ===")
    all_investors = Investor.get_all(session)
    for investor in all_investors:
        print(f"- {investor.id}: {investor.name} ({investor.firm})")

    session.close()

if __name__ == "__main__":
    run_debug()

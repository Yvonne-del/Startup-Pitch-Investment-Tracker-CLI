from lib.models.startup import Startup
from lib.models.pitch import Pitch
from lib.models.investor import Investor

from lib.helpers import get_session, calculate_average_interest, get_most_interested_investors
from datetime import datetime


# Main menu
def display_menu():
    print("\nStartup pitch & Investment Tracker")
    print("1. Manage Startups")
    print("2. Manage Pitches")
    print("3. Manage Investors")
    print("4. Fundraising Insights")
    print("0. Exit")
    
# startup management operations
def manage_startups(session):
    while True:
        print("\nStartups Menu:")
        print("1. Add Startup")
        print("2. View All Startups")
        print("3. Delete Startup")
        print("0. Back")
        
        choice = input("> ")
        if choice == "1":
            name = input("Enter startup name: ")
            desc = input("Enter description: ")
            stage = input("Enter funding stage: ")
            Startup.create(session, name, desc, stage)
            print("Startup added!")
        elif choice == "2":
            startups = Startup.get_all(session)
            for s in startups:
                print(f"ID: {s.id}, Name: {s.name}, Stage: {s.funding_stage}")
        elif choice == "3":
            id = int(input("Enter startup ID to delete: "))
            Startup.delete(session, id)
            print("startup deleted successfully")
        elif choice == "0":
            break
        else:
            print("Invalid choice.")

# pitches management operations
def manage_pitches(session):
    while True:
        print("\nPitches Menu:")
        print("1. Add Pitch")
        print("2. View Pitches for Startup")
        print("3. Delete Pitch")
        print("0. Back")
        choice = input(">")
        if choice == "1":
            startup_id = int(input("Enter startup ID: "))
            investor_id = int(input("Enter investor ID: "))
            date = datetime.strptime(input("Enter date (YYYY-MM-DD): "), "%Y-%m-%d")
            feedback = input("Enter feedback: ")
            rating = int(input("Enter interest rating (0-5): "))
            Pitch.create(session, startup_id, investor_id, date, feedback, rating)
            print("Pitch added.")
        elif choice == "2":
            startup_id = int(input("Enter startup ID: "))
            pitches = Pitch.get_all_for_startup(session, startup_id)
            for p in pitches:
                print(f"ID: {p.id}, Investor: {p.investor.name}, Date: {p.date}, Rating: {p.interest_rating}")
        elif choice == "3":
            id = int(input("Enter pitch ID to delete: "))
            Pitch.delete(session, id)
            print("Pitch deleted successfully.")
        elif choice == "0":
            break
        else:
            print("Invalid choice.")
            
            
# investors management operations
def manage_investors(session):
    while True:
        print("\nInvestors Menu:")
        print("1. Add Investor")
        print("2. View All Investors")
        print("3. Delete Investor")
        print("0. Back")
        choice = input("> ")
        if choice == "1":
            name = input("Enter investor name: ")
            firm = input("Enter firm: ")
            sector = input("Enter sector focus: ")
            Investor.create(session, name, firm, sector)
            print("Investor added!")
        elif choice == "2":
            investors = Investor.get_all(session)
            for inv in investors:
                print(f"ID: {inv.id}, Name: {inv.name}, Firm: {inv.firm}, Sector: {inv.sector_focus}")
        elif choice == "3":
            id = int(input("Enter investor ID to delete: "))
            Investor.delete(session, id)
            print("Investor deleted successfully.")
        elif choice == "0":
            break
        else:
            print("Invalid choice.")

# fundraising operations
def fundraising_insights(session):
    while True:
        print("\nFundraising Insights Menu:")
        print("1. Average Investor Interest for Startup")
        print("2. Top 3 Interested Investors for Startup")
        print("0. Back")
        choice = input("> ")
        if choice == "1":
            startup_id = int(input("Enter startup ID: "))
            avg_interest = calculate_average_interest(session, startup_id)
            print(f"Average Interest Rating: {avg_interest:.2f}")
        elif choice == "2":
            startup_id = int(input("Enter startup ID: "))
            top_pitches = get_most_interested_investors(session, startup_id)
            print("Top Interested Investors:")
            for p in top_pitches:
                print(f"Investor: {p.investor.name}, Rating: {p.interest_rating}")
        elif choice == "0":
            break
        else:
            print("Invalid choice.")

# Main function
def main():
    session = get_session()
    while True:
        display_menu()
        # pass the choices
        choice = input("> ")
        if choice == "1":
            manage_startups(session)
        elif choice == "2":
            manage_pitches(session)
        elif choice == "3":
            manage_investors(session)
        elif choice == "4":
            fundraising_insights(session)
        elif choice == "0":
            session.close()
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

      
if __name__ == "__main__":
    main()
# Startup Pitch & Investment Tracker
This is a command-line application built in Python using SQLAlchemy to track startups, investors, and their pitch interactions.

It allows you to:
    Add, view, and delete startups
    Add, view, and delete investors
    Record pitches and track investor interest
    Get insights into fundraising progress

# Table of Contents
    Features
    Project Structure
    Setup Instructions
    Usage
    Seeding the Database
    Running Debug Tests
    Dependencies



# Features
Startups: Add, view, delete startups with details such as name, description, and funding stage.

Investors: Add, view, delete investors, including their name, firm, and investment focus.

Pitches: Record pitches made to investors, including feedback and interest rating.

Insights: Calculate average investor interest and identify top interested investors for each startup.

# Project Structure

/Investor-tracker
│
├── db/
│   └── seed.py        
├── lib/
    ├── models/
    |    ├── __init__.py    # SQLAlchemy setup (Base, engine, session)
│   |    ├── startup.py     # Startup model
│   |    ├── investors.py   # Investor model
│   |    └── pitch.py       # Pitch model
│   ├── cli.py         # Main CLI interface
│   ├── helpers.py     # Helper functions (session management, calculations)
│   └── debug.py       # Script to manually test models and relationships


# Setup Instructions
Clone the repository

    git clone <repository-url>
    cd <repository-folder>

Set up a virtual environment

    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate

Install dependencies

    pip install -r requirements.txt

Set up the database

    Make sure your models/__init__.py points to a valid SQLite file (or another database of your choice).

    To initialize the database:


        from models import Base, engine
        Base.metadata.create_all(engine)

# Usage
To run the main CLI interface:

    python lib/cli.py

You will see a menu allowing you to manage startups, investors, pitches, and fundraising insights.

Seeding the Database
To populate the database with sample data for testing:

    python db/seed.py
        or
    python -m lib.cli    #if you get an errorwith the first one

This will add:

    3 example startups

    3 example investors

    10 random pitches

Running Debug Tests
If you want to manually test creating and fetching records:

    python lib/debug.py

This script will:
    Create a sample startup, investor, and pitch
    Fetch and display all startups and investors in the database

# Dependencies
This project uses:
    Python 3.x
    SQLAlchemy
    datetime (Python standard library)

Make sure all dependencies are listed in requirements.txt. Example content:

    SQLAlchemy==2.x

You can generate this file by running:

    pip freeze > requirements.txt


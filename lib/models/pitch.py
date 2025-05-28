# holds the pitch idea model
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from . import Base

class Pitch(Base):
    __tablename__ = "pitches"
    
    # columns: id, startup_id, investors_id, date, feedback, interest_rating
    
    id = Column(Integer, primary_key=True)
    startup_id = Column(Integer, ForeignKey("startups.id"), nullable=False)
    investor_id = Column(Integer, ForeignKey("investors.id"), nullable=False)
    date = Column(Date, nullable=False)
    feedback = Column(String)
    # interest (0-5)
    interest_rating = Column(Integer)
    
    # relationships with Startup and Investor
    startup = relationship("Startup", back_populates="pitches")
    investor = relationship("Investor", back_populates="pitches")
    
    # create a new pitch
    @classmethod
    def create(cls, session, startup_id, investor_id, date, feedback, interest_rating):
        if not (0 <= interest_rating <= 5):
            raise ValueError("Interest rating must be between 0 and 5")
        pitch = cls(startup_id=startup_id,
        investor_id=investor_id,
        date=date,
        feedback=feedback,
        interest_rating=interest_rating)
        session.add(pitch)
        session.commit()
        return pitch
    
    # retrieve all pitches for a startup
    @classmethod
    def get_all_for_startup(cls, session, startup_id):
        return session.query(cls).filter_by(startup_id=startup_id).all()
    
    # retrieve all pitches for an investor
    @classmethod
    def get_all_for_investors(cls, session, investor_id):
        return session.query(cls).filter_by(investor_id=investor_id).all()
    
    # find a pitch by ID
    @classmethod
    def find_by_id(cls, session, id):
        return session.query(cls).filter_by(id=id).first()
    
    # delete a pitch by ID
    @classmethod
    def delete(cls, session, id):
        pitch = cls.find_by_id(session, id)
        if pitch:
            session.delete(pitch)
            session.commit()
        return pitch
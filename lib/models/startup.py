from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Startup(Base):
    __tablename__ = "startups"
    
    # Columns: id, name, description, funding
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    funding_stage = Column(String)
    
    # one to many relationship with the pitch
    pitches = relationship("Pitch", back_populates="startup", cascade='all, delete-orphan')
    
    # property to count associated pitches
    @property
    def pitch_count(self):
        return len(self.pitches)
    
    # create a new startup
    @classmethod
    def create(cls, session, name, description, funding_stage):
        startup = cls(name=name, description=description, funding_stage=funding_stage)
        session.add(startup)
        session.commit()
        return startup
    
    # retrieve all startups
    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()    
    
    # find a startup by ID
    @classmethod
    def find_by_id(cls, session, id):
        return session.query(cls).filter_by(id=id).first()    
    
    # delete a startup by ID
    @classmethod
    def delete(cls, session, id):
        startup = cls.find_by_id(session, id)
        if startup:
            session.delete(startup)
            session.commit()
        return startup
    
    


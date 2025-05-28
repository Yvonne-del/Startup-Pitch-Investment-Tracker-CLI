from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class Investor(Base):
    # __table__ = "investors"
    __tablename__ = "investors"
    
    # columns: id, name, firm, sector
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    firm = Column(String)
    sector_focus = Column(String)
    
    # one-to-many relationship with Pitch
    pitches = relationship("Pitch", back_populates="investor")
    
    # create a new investor
    @classmethod
    def create(cls, session, name, firm, sector_focus):
        investor = cls(name=name, firm=firm, sector_focus=sector_focus)
        session.add(investor)
        session.commit()
        return investor
    
    # retrieve all investors
    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()
    
    # find an investor by ID
    @classmethod
    def find_by_id(cls, session, id):
        return session.query.filter_by(id=id).first()
    
    # delete an investor by ID
    @classmethod
    def delete(cls, session, id):
        investor = cls.find_by_id(session, id)
        if investor:
            session.delete(investor)
            session.commit()
        return investor
    
    
    
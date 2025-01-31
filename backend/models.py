from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean
from db import engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

class YouTubeAccount(Base):
    __tablename__ = 'youtube_accounts'
    id = Column(Integer, primary_key=True, index=True)
    region = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

Base.metadata.create_all(bind=engine)

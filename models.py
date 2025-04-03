#representação do banco de dados, onde fica localizado o sqmalchemy
#onde é criada a tabela

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from db import Base

class Cars(Base):
    __tablename__ = 'carros'
    id = Column(Integer, primary_key = True, index = True)
    cylinders = Column(Integer)
    make = Column(String)
    model = Column(String)
    created_at = Column(DateTime, default=func.now())

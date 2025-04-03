#onde são criadas as funções
import requests
from db import SessionLocal, engine, Base
from models import Cars
from schema import CarSchema

Base.metadata.create_all(bind=engine)

def get_cars(nome_carro: str) -> CarSchema:
    URL = f"https://cars-by-api-ninjas.p.rapidapi.com/v1/cars?model={nome_carro}"
    HEADERS = {
    "x-rapidapi-host": "cars-by-api-ninjas.p.rapidapi.com",
    "x-rapidapi-key": "b12ad3ba07msh557bea3e910a1e9p1fe57ajsn3a9f2768fe40"
}
    response = requests.get(url=URL, headers=HEADERS)
    if response.status_code == 200:
        data = response.json()[0]
        dicionario_cars = {}
        dicionario_cars['cylinders'] = response.json()[0]['cylinders']
        dicionario_cars['make'] = response.json()[0]['make']
        dicionario_cars['model'] = response.json()[0]['model']
        return CarSchema(cylinders = dicionario_cars['cylinders'], make = dicionario_cars['make'], model = dicionario_cars['model'])
    else:
        return None

def add_cars_db(car_schema: CarSchema) -> Cars:
    with SessionLocal() as db:
        db_cars = Cars(make = car_schema.make, cylinders = car_schema.cylinders, model = car_schema.model)
        db.add(db_cars)
        db.commit()
        db.refresh(db_cars)
    return db_cars

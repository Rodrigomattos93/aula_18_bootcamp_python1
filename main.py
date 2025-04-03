import time
from controller import get_cars, add_cars_db

def main():
    while True:
        cars_schema = get_cars('corolla')
        if cars_schema:
            print(f"Adicionando {cars_schema.model} ao banco de dados")
            add_cars_db(cars_schema)
        else:
            print(f"Não foi possível obter dados para o carro solicitado")
        time.sleep(10)

if __name__ == "__main__":
    main()
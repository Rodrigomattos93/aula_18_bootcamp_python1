#o schema também é chamado de contrato de dados ou view

from pydantic import BaseModel

class CarSchema(BaseModel):
    cylinders: int
    make: str
    model: str

    class Config:
        from_attributes = True

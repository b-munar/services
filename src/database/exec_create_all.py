from src.database.base import Base
from src.database.engine import engine

from src.models.service_model import ServiceModel, Sportmen

table_objects = [ServiceModel.__table__, Sportmen.__table__]

if __name__ == "__main__":
    Base.metadata.create_all(
        bind = engine(), 
        tables=table_objects,
        checkfirst=True
    )
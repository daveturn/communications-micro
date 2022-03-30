from cassandra.cqlengine.models import Model
from app.app.core.config import settings



class BaseModel(Model):
    __abstract__ = True
    __keyspace__ = settings.KEYSPACE_NAME

    def to_json(self):
        return {k:v for k,v in self.items()}


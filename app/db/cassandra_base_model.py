from cassandra.cqlengine.models import Model


class BaseModel(Model):
    __abstract__ = True
    __keyspace__ = "KEYSPACE_NAME"

    def to_json(self):
        return {k: v for k, v in self.items()}

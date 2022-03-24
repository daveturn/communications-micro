# db

Any general methods or values related to database connections should be saved here.

This repo uses the [SQLModel](https://sqlmodel.tiangolo.com/) library, which is a wrapper for SQLAlchemy. It was developed by the same team as FastAPI in order to make database models more similar to general Pydantic syntax.

### Initialization

The exported `get_session` function in `init_db.py` takes one argument, the name of the database, which should be declared in the `DatabaseName` enum class. Calling `get_session` with the correct name should be sufficient to create the connection for interacting with the database.

```python

from app.app.db.init_db import  get_session, DatabaseName

database_session = get_session(DatabaseName.DATABASE)

```

### BaseModel

The model in `base_model.py` is intended to be a place to store values and methods which will be shared across all models.

### Alembic

Alembic and SQLModel reference the `base.py` file to determine which models to consider when auto-generating migration files. Make sure that all models that you want to see in the database are imported here.

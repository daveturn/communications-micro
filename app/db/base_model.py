from typing import Union
import pydantic
from sqlmodel import SQLModel, Session
from .constants import SCHEMA_NAME


class BaseSQLModel(SQLModel):
    """
    Base class containing method which will be useful for all Models.

    If a model will represent a table in the database, it must be declared with
    an additional parameter `table=True` eg:

    class PartnerWorkerModelReadOnly(BaseSQLModel, table=True):
    """

    __table_args__ = {
        "schema": SCHEMA_NAME
    }  # remove this if you would like to reference the default 'public' schema
    # for your models.

    async def save(self, db: Session):
        db.add(self)
        db.commit()
        return self

    async def delete(self, db: Session):
        db.delete(self)
        db.commit()

    def model_is_equal_to(
        self, model: Union[SQLModel, pydantic.BaseModel]
    ) -> bool:
        """
        See if a model needs to be updated by comparing it to a newer version
        """
        if not model:
            return False
        this_dict = self.dict()
        compare_dict = model.dict()

        for k, v in this_dict.items():
            if not hasattr(compare_dict, k):
                return False
            attr = getattr(compare_dict, k)
            if v != attr:
                return False

        return True

    def update_from_model(self, model: SQLModel):
        this_dict = self.dict()
        compare_dict = model.dict()

        for k, v in this_dict.items():
            if not hasattr(compare_dict, k):
                continue
            attr = getattr(compare_dict, k)
            if v != attr:
                setattr(self, k, attr)

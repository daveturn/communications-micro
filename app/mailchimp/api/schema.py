from typing import Optional
from pydantic import BaseModel, validator

from app.app.utils.validators.zipcode import validate_zipcode


class AddEmailPostPayload(BaseModel):
    email: str
    zipcode: str
    posting_id: str
    mailchimp_list_id: Optional[str] = None

    @validator("zipcode")
    def zipcodes_must_be_valid(cls, value: str) -> str:
        return validate_zipcode(value)

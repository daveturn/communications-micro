from typing import Optional
from pydantic import BaseSettings
import logging

logger = logging.getLogger(__name__)


class Settings(BaseSettings):
    INTERNAL_API_KEY: str
    MAILCHIMP_API_KEY: str
    MAILCHIMP_DATACENTER: str
    MAILCHIMP_DEFAULT_AUDIENCE_ID: Optional[str] = None

    MANDRILL_API_KEY: str
    MANDRILL_API_BASE_URL: str = "https://mandrillapp.com/api/1.0"
    MANDRILL_DEFAULT_FROM_EMAIL: str
    MANDRILL_DEFAULT_FROM_NAME: str


settings = Settings()  # type: ignore

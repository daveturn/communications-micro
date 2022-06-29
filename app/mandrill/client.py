from typing import Dict, List

import requests
from app.core.config import settings
from app.mandrill.schema import MandrillMessage, MandrillRecipientEntry
from app.utils.api_connector_base import ApiConnectorBaseClass


class MandrillClient(ApiConnectorBaseClass):
    __slots__ = ("base_url", "api_key")
    base_url: str
    api_key: str

    def __init__(self, name: str = "mandrill", *, api_key: str) -> None:
        super().__init__(name)
        self.base_url = settings.MANDRILL_API_BASE_URL
        self.api_key = api_key

    def _call_api(self, url: str, body: Dict, *args, **kwargs):
        super()._call_api(*args, **kwargs)
        full_body = {**body, "key": self.api_key}
        _url = self.base_url + url
        res = requests.post(url=_url, json=full_body)
        self._validate_response(res)
        return res.json()

    def send_message(
        self, *, subject: str, html: str, to: List[MandrillRecipientEntry]
    ):
        url = "/messages/send"
        message = MandrillMessage(
            subject=subject,
            to=to,
            html=html,
            from_email=settings.MANDRILL_DEFAULT_FROM_EMAIL,
            from_name=settings.MANDRILL_DEFAULT_FROM_NAME,
        )
        return self._call_api(url=url, body={"message": message.dict()})

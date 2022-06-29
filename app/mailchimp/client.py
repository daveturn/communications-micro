from typing import Any, Dict, Literal, Optional
import requests
from requests import Response
from .schema import AddMemberToListPayload

from app.utils.api_connector_base import (
    ApiConnectorBaseClass,
    ApiConnectorResponseException,
)


class MailchimpClientException(ApiConnectorResponseException):
    pass


class MailchimpClient(ApiConnectorBaseClass):
    __slots__ = ("base_url", "session")
    base_url: str
    session: requests.Session

    def __init__(
        self, name: str = "mailchimp", *, datacenter: str, api_key: str
    ) -> None:
        super().__init__(name)
        self.base_url = f"https://{datacenter}.api.mailchimp.com/3.0"
        session = requests.Session()
        session.auth = ("x", api_key)
        self.session = session

    def __prepare_url(self, raw_url: str):
        """
        To make this able to handle relative and complete urls,
        this method checks if the raw_url string contains "http" and if not,
        it prepends the stored base_url
        """
        if "http" in raw_url.lower():
            return raw_url
        return self.base_url + raw_url

    def _call_api(
        self,
        *,
        url: str,
        method: Literal["GET", "POST"],
        json: Optional[Dict[str, Any]] = None,
    ) -> Response:
        super()._call_api(url=url, method=method, json=json)
        _url = self.__prepare_url(url)
        response = self.session.request(url=_url, method=method, json=json)
        return self._validate_response(response)

    def add_member_to_audience(
        self, list_id: str, payload: AddMemberToListPayload
    ):
        url = f"/lists/{list_id}/members"

        response = self._call_api(url=url, method="POST", json=payload.dict())
        return response.json()

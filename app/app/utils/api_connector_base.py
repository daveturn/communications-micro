from abc import ABC, abstractmethod, abstractproperty
from dataclasses import dataclass
from typing import  Optional, Literal
from enum import Enum

import requests
import logging

logger = logging.Logger(__name__)

class HTTPMethod(str, Enum):
    GET: Literal['GET'] = 'GET'
    POST: Literal['POST'] = 'POST'
    PUT: Literal['PUT'] = 'PUT'
    PATCH: Literal['PATCH'] = 'PATCH'


class ApiConnectorResponseException(Exception):
    def __init__(self, response: requests.models.Response, message: str):
        logger.info(
            message
        )
        super.__init__(message)

class ApiConnectorResponseNotFoundException(ApiConnectorResponseException):
    pass

class ApiConnectorResponseServerErrorException(ApiConnectorResponseException):
    pass


class ApiConnectorBaseClass(ABC):
    '''
        Abstract Base class for common attibutes and methods relating to dealing with external APIs.
    '''
    base_url = ''

    def __init__(self, name: str, **kwargs) -> None:
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, val: str):
        self._name = val

    @abstractmethod
    def _call_api(
            self, 
            *args,
            **kwargs):
        pass

    @classmethod
    def _validate_response(cls, response: requests.models.Response):
        status_code = response.status_code
        if status_code < 300:
            return response

        if status_code == 404:
            raise ApiConnectorResponseNotFoundException(
                response=response,
                message=f'{cls.name}: {response.url}'
            )

        if status_code >= 500:
            raise ApiConnectorResponseServerErrorException(
                response=response,
                message=f'{cls.name}: {response.url}'
            )

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
import logging

logger = logging.Logger(__name__)


class AsyncIteratorWrapper:
    def __init__(self, obj):
        self._it = iter(obj)

    def __aiter__(self):
        return self

    async def __anext__(self):
        try:
            value = next(self._it)
        except StopIteration:
            raise StopAsyncIteration
        return value


class LoggingMiddleware(BaseHTTPMiddleware):
    """
    Logs request and response details for unsuccessful API calls
    """

    def __init__(self, app):
        super().__init__(app)

    async def set_body(self, request: Request):
        receive_ = await request._receive()

        async def receive():
            return receive_

        request._receive = receive

    async def dispatch(self, request: Request, call_next):
        await self.set_body(request)
        res: Response = await call_next(request)
        if res.status_code > 299:
            body = await request.body() if hasattr(request, "body") else None
            # Consuming FastAPI response and grabbing body here
            res_body = [
                section async for section in res.__dict__["body_iterator"]
            ]
            # Repairing FastAPI response
            res.__setattr__("body_iterator", AsyncIteratorWrapper(res_body))
            logger.info(
                f"""
Status: {res.status_code}
URL: {request.url}
Body: {body}

RESPONSE
{res_body}
"""
            )
        return res

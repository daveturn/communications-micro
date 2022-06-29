from fastapi import APIRouter, Depends

from app.auth.internal_auth import check_internal_auth
from app.mandrill.api.schema import SendMandrillMessagePayload


mandrill_router = APIRouter(
    prefix="/mailchimp",
    tags=["mailchimp"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(check_internal_auth)],
)


@mandrill_router.post("")
def send_mandrill_message(payload: SendMandrillMessagePayload):
    pass

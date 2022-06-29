from fastapi import APIRouter, Depends

from app.auth.internal_auth import check_internal_auth
from app.mailchimp.client import MailchimpClient
from app.mailchimp.schema import AddMemberToListPayload
from app.core.config import settings


mailchimp_router = APIRouter(
    prefix="/mailchimp",
    tags=["mailchimp"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(check_internal_auth)],
)


@mailchimp_router.post(
    "/add_contact_to_audience/{list_id}",
    description=(
        """
        Add a new contact to an existing audience list in Mailchimp.
        """
    ),
    name="Add member to audience",
    tags=["mailchimp", "communications"],
)
def add_email(
    list_id: str,
    add_email_payload: AddMemberToListPayload,
):

    mailchimp = MailchimpClient(
        api_key=settings.MAILCHIMP_API_KEY,
        datacenter=settings.MAILCHIMP_DATACENTER,
    )
    return mailchimp.add_member_to_audience(
        list_id=list_id, payload=add_email_payload
    )

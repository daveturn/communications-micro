import vcr
import pytest
from app.core.config import Settings

from app.mandrill.client import MandrillClient
from app.mandrill.schema import MandrillRecipientEntry

base_vcr = vcr.VCR(
    cassette_library_dir="tests/mandrill/cassettes",
    ignore_localhost=True,
    record_mode="once",
)


@pytest.fixture
def mandrill_client(app_settings: Settings):
    return MandrillClient(api_key=app_settings.MANDRILL_API_KEY)


class TestMandrillClient:
    def test_mandrill_client_sends_email(
        self, mandrill_client: MandrillClient
    ):

        with base_vcr.use_cassette("send_message_1.yml"):
            recipient = MandrillRecipientEntry(email="david@turn.ai")
            res = mandrill_client.send_message(
                html="<p>Hello</p>", subject="test", to=[recipient]
            )
            assert res
            assert res["status"] == "sent"

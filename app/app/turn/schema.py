

from lib2to3.pgen2.token import OP
from typing import List, Optional, Union
from uuid import UUID

from pydantic import BaseModel
from datetime import datetime


class PartnerWorkerSchema(BaseModel):
    id: int
    worker_id: Optional[str]
    partner_id: int
    profile_status: Optional[str]
    worker_consent: Optional[str]
    worker_assent: Optional[str]
    date_of_birth: Optional[datetime]
    create_timestamp: Optional[datetime]
    search_data_id: Union[int, str]
    uuid: Optional[str]
    location_id: Optional[str]
    person_search_callback_id: Optional[str]
    deceased_date: Optional[datetime]
    drivers_license_number: Optional[str]
    drivers_license_state: Optional[str]
    intuit_id: Optional[str]
    is_county_criminal_report_updated: Optional[str]
    gender: Optional[str]
    zipcode: Union[int, str]
    fountain_id: Optional[str]
    wss_subject_id: Optional[str]
    is_manual_background_check: Optional[str]
    manual_background_check_report_url: Optional[str]
    is_mvr_report_updated: Optional[str]
    reference_id: Optional[str]
    is_ssn_deceased: int
    is_ssn_random: int
    is_ssn_valid: int
    turn_id: Optional[str]
    workflow_turn_id: Optional[str]
    workflow_package_id: Optional[str]
    finish_review: Optional[str]
    check_status: Optional[str]
    consent_date: Optional[str]
    updated_by: Optional[Union[int, str]] = None
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    middle_name: Optional[str] = None
    phone_number: Optional[int] = None
    note: Optional[str] = None

class PartnerSchema(BaseModel):
    id: int
    name: str
    end_trial: Optional[datetime]
    start_trial: Optional[datetime]
    is_trial: bool
    trial_limit: Optional[int]
    webhook_url: Optional[str]
    autoapprove: Optional[bool]
    uuid: Optional[UUID]
    do_intuit: Optional[bool]
    intuit_password: Optional[any]
    intuit_username: Optional[any]
    firebase_id: Optional[str]
    adverse_action: Optional[bool]
    default_package_id: Optional[int]
    inactive: Optional[bool]
    description: Optional[str]
    icon_url: Optional[str]
    is_turn_partner: Optional[bool]
    laniidae_token: Optional[str]
    _use_laniidae: Optional[bool]
    is_send_ssn_trace_email_to_candidate: Optional[bool]
    ask_for_assent: Optional[bool]
    unique_code: Optional[str]
    billing_type: Optional[str]
    ecommerce_type: Optional[str]
    default_days_range: Optional[int]
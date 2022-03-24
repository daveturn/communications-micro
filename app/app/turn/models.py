
from abc import abstractmethod
from typing import List, Optional, Union
from datetime import datetime
from pydantic import UUID4
from sqlalchemy_utils import (
    UUIDType
)

from sqlalchemy import Integer, Column
from sqlmodel import Field

from app.app.db.base_model import BaseSQLModel

class FreshdeskTableModel(BaseSQLModel):
    __table_args__ = {'schema': 'freshdesk'}
    

    @staticmethod
    @abstractmethod
    def load_from_read_only_model(read_only_model: BaseSQLModel) -> 'FreshdeskTableModel':
        pass

class PartnerWorkerModelReadOnly(BaseSQLModel, table=True):
    __table_args__ = {'schema': 'public'}
    __tablename__ = 'partner_worker'
    id: int = Field(sa_column=Column(Integer(), primary_key=True, autoincrement=False))
    worker_id: Optional[str]
    partner_id: int
    profile_status: Optional[str]
    worker_consent: Optional[str]
    worker_assent: Optional[str]
    date_of_birth: Optional[datetime]
    create_timestamp: Optional[datetime]
    search_data_id: Optional[str]
    uuid: Optional[str]
    location_id: Optional[str]
    person_search_callback_id: Optional[str]
    deceased_date: Optional[datetime]
    drivers_license_number: Optional[str]
    drivers_license_state: Optional[str]
    intuit_id: Optional[str]
    is_county_criminal_report_updated: Optional[str]
    gender: Optional[str]
    zipcode: Optional[str]
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
    updated_by: Optional[str]
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    middle_name: Optional[str] = None
    phone_number: Optional[str] = None
    note: Optional[str] = None


# I can't work out why but I couldn't get this to work by inheriting the class above
# Apologies for duplicated code
class PartnerWorkerModel(FreshdeskTableModel, table=True):
    __tablename__ = 'partner_worker'
    id: int = Field(sa_column=Column(Integer(), primary_key=True))
    worker_id: Optional[str]
    partner_id: int
    profile_status: Optional[str]
    worker_consent: Optional[str]
    worker_assent: Optional[str]
    date_of_birth: Optional[datetime]
    create_timestamp: Optional[datetime]
    search_data_id: Optional[str]
    uuid: Optional[str]
    location_id: Optional[str]
    person_search_callback_id: Optional[str]
    deceased_date: Optional[datetime]
    drivers_license_number: Optional[str]
    drivers_license_state: Optional[str]
    intuit_id: Optional[str]
    is_county_criminal_report_updated: Optional[str]
    gender: Optional[str]
    zipcode: Optional[str]
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
    updated_by: Optional[str]
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    middle_name: Optional[str] = None
    phone_number: Optional[str] = None
    note: Optional[str] = None


    @staticmethod
    def load_from_read_only_model(read_only_model: PartnerWorkerModelReadOnly) -> 'PartnerWorkerModel':
        model = PartnerWorkerModel(
            **read_only_model.dict()
        )        
        return model


class PartnerModelReadOnly(BaseSQLModel, table=True):
    __table_args__ = {'schema': 'public'}
    __tablename__ = 'partner'
    id: int = Field(sa_column=Column(Integer(), primary_key=True, autoincrement=False))
    name: str
    end_trial: Optional[datetime]
    start_trial: Optional[datetime]
    is_trial: bool
    trial_limit: Optional[int]
    webhook_url: Optional[str]
    autoapprove: Optional[bool]
    uuid: UUID4 = Field(sa_column=Column(UUIDType(binary=False), nullable=True, unique=True))
    do_intuit: Optional[bool]
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


class PartnerModel(FreshdeskTableModel, table=True):
    __tablename__ = 'partner'
    id: int = Field(sa_column=Column(Integer(), primary_key=True))
    name: str
    end_trial: Optional[datetime]
    start_trial: Optional[datetime]
    is_trial: bool
    trial_limit: Optional[int]
    webhook_url: Optional[str]
    autoapprove: Optional[bool]
    uuid: UUID4 = Field(sa_column=Column(UUIDType(binary=False), nullable=True, unique=True))
    do_intuit: Optional[bool]
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

    @staticmethod
    def load_from_read_only_model(read_only_model: PartnerModelReadOnly) -> 'PartnerModel':
        model = PartnerModel(
            **read_only_model.dict()
        )        
        return model

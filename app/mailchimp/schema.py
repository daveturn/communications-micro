from typing import Dict, List, Any, Literal, Optional, Union
from pydantic import BaseModel


class AddMemberToListPayload(BaseModel):
    email_address: str
    email_type: Optional[Literal["html", "text"]] = "html"
    status: Optional[
        Literal[
            "subscribed", "unsubscribed", "cleaned", "pending", "transactional"
        ]
    ] = "subscribed"
    merge_fields: Dict[str, Union[str, int, float, None]]
    interests: Dict[str, Union[str, int, float, None]] = {}
    language: Optional[str] = ""
    vip: bool = False
    location: Dict[str, Union[str, int, float, None]] = {}
    marketing_permissions: List[Any] = []
    ip_signup: Optional[str] = ""
    timestamp_signup: Optional[str] = ""
    ip_opt: Optional[str] = ""
    timestamp_opt: Optional[str] = ""
    tags: List[str] = []

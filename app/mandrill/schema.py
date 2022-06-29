from typing import Any, Dict, List, Literal, Optional
from pydantic import BaseModel


class MandrillRecipientEntry(BaseModel):
    email: str
    name: Optional[str] = None
    type: Optional[Literal["to", "cc", "bcc"]] = "to"


class MandrillMergeVarEntry(BaseModel):
    name: str
    content: str


class MandrillMergeVarPerRecipient(BaseModel):
    rcpt: str  # the email address of the
    # recipient that the merge variables should apply to
    vars: List[MandrillMergeVarEntry]


class MandrillMessage(BaseModel):
    html: str
    text: Optional[str] = None
    subject: str
    from_email: str
    from_name: str
    to: List[MandrillRecipientEntry]
    headers: Optional[Dict[str, Any]] = None
    important: Optional[bool] = False
    track_opens: Optional[bool] = True
    track_clicks: Optional[bool] = True
    auto_text: Optional[bool] = True
    auto_html: Optional[bool] = True
    inline_css: Optional[bool] = False
    url_strip_qs: Optional[bool] = False
    preserve_recipients: Optional[bool] = False
    view_content_link: Optional[bool] = False
    bcc_address: Optional[str] = None
    tracking_domain: Optional[str] = None
    signing_domain: Optional[str] = None
    return_path_domain: Optional[str] = None
    merge: Optional[bool] = True
    merge_language: Optional[str] = None
    global_merge_vars: Optional[List[MandrillMergeVarEntry]] = None
    # global merge variables to use
    # for all recipients. You can override these per recipient.
    merge_vars: Optional[List[MandrillMergeVarPerRecipient]] = None
    tags: Optional[List[str]] = None
    subaccount: Optional[str] = None
    google_analytics_domains: Optional[List[str]] = None
    google_analytics_campaign: Optional[str] = None

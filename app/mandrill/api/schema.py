from typing import List, Optional
from app.mandrill.schema import MandrillMergeVarEntry, MandrillRecipientEntry


class SendMandrillMessagePayload:
    to: List[MandrillRecipientEntry]
    subject: str
    html: str
    text: Optional[str] = None
    global_merge_vars: Optional[List[MandrillMergeVarEntry]] = None

from pydantic import BaseModel
from typing import List, Optional

class Stakeholder(BaseModel):
    name: str
    role: str
    description: Optional[str]

class NegotiationInput(BaseModel):
    scenario: str
    negotiation_type: str
    stakeholders: List[Stakeholder]
    frameworks: List[str]

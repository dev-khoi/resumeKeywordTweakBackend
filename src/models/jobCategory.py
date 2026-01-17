from typing import Optional
from pydantic import BaseModel


class AiJobCategory(BaseModel):
    company: Optional[str] = None
    position_title: Optional[str] = None
    location: Optional[str] = None
    min_salary: Optional[float] = None
    max_salary: Optional[float] = None
    currency_type: Optional[str] = None
    pay_period: Optional[str] = None
    job_type: Optional[str] = None
    job_description: Optional[str] = None
    notes: Optional[str] = None

from datetime import date, datetime
from pydantic import BaseModel, Field


class RateResponse(BaseModel):
    base: str
    quote: str
    rate: float
    date: date


class ConvertRequest(BaseModel):
    source: str = Field(min_length=3, max_length=3)
    target: str = Field(min_length=3, max_length=3)
    amount: float = Field(gt=0)


class ConvertResponse(BaseModel):
    source: str
    target: str
    amount: float
    converted_amount: float
    rate: float
    chain: list[str]


class ConversionHistoryResponse(BaseModel):
    id: int
    source_currency: str
    target_currency: str
    amount: float
    converted_amount: float
    rate: float
    created_at: datetime

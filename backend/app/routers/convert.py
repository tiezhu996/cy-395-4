from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from app.models.base import get_db
from app.schemas.exchange import ConvertRequest
from app.services.exchange_service import convert, list_conversion_history

router = APIRouter(prefix="/api/v1/convert", tags=["货币换算"])


@router.post("")
def convert_currency(payload: ConvertRequest, request: Request, db: Session = Depends(get_db)):
    return convert(db, payload.source, payload.target, payload.amount, request.state.client_id)


@router.get("/history")
def get_history(request: Request, db: Session = Depends(get_db)):
    return list_conversion_history(db, request.state.client_id)

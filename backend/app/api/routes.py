from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.responses import (
    MarketResponse,
    ReviewResponse,
    RiskResponse,
    ScannerResponse,
    SectorResponse,
    TradePlanResponse,
)
from app.services.data_service import (
    get_latest_market,
    get_latest_review,
    get_latest_risk,
    get_latest_scanner,
    get_latest_sectors,
    get_latest_trade_plan,
)

router = APIRouter(prefix="/api", tags=["api"])


@router.get("/market", response_model=MarketResponse)
def market(db: Session = Depends(get_db)):
    item = get_latest_market(db)
    return {
        "date": item.date,
        "market_regime": item.market_regime,
        "risk_level": item.risk_level,
        "recommended_exposure": item.recommended_exposure,
        "summary": item.summary,
    }


@router.get("/sectors", response_model=list[SectorResponse])
def sectors(db: Session = Depends(get_db)):
    return get_latest_sectors(db)


@router.get("/scanner", response_model=list[ScannerResponse])
def scanner(db: Session = Depends(get_db)):
    return get_latest_scanner(db)


@router.get("/trade-plan", response_model=list[TradePlanResponse])
def trade_plan(db: Session = Depends(get_db)):
    return get_latest_trade_plan(db)


@router.get("/risk", response_model=RiskResponse)
def risk(db: Session = Depends(get_db)):
    item = get_latest_risk(db)
    return {
        "risk_level": item.risk_level,
        "accountA_exposure": item.accounta_exposure,
        "accountB_exposure": item.accountb_exposure,
        "drawdown_today_pct": item.drawdown_today_pct,
        "action_suggestion": item.action_suggestion,
    }


@router.get("/review", response_model=ReviewResponse)
def review(db: Session = Depends(get_db)):
    return get_latest_review(db)

from datetime import date

from pydantic import BaseModel


class MarketResponse(BaseModel):
    date: date
    market_regime: str
    risk_level: str
    recommended_exposure: float
    summary: str


class SectorResponse(BaseModel):
    sector: str
    sector_strength: float
    flow_state: str
    one_liner: str


class ScannerResponse(BaseModel):
    name: str
    ticker: str
    sector: str
    trend_score: float
    rs_score: float
    flow_score: float
    total_score: float


class TradePlanResponse(BaseModel):
    name: str
    ticker: str
    action: str
    planned_position_pct: float
    entry_condition: str
    stop_loss: str


class RiskResponse(BaseModel):
    risk_level: str
    accountA_exposure: float
    accountB_exposure: float
    drawdown_today_pct: float
    action_suggestion: str


class ReviewResponse(BaseModel):
    plan_adherence: str
    good: str
    bad: str
    fixes: str
    tomorrow_focus: str

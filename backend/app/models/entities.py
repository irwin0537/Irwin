from datetime import datetime, date

from sqlalchemy import Date, DateTime, Float, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class MarketDaily(Base):
    __tablename__ = "market_daily"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    date: Mapped[date] = mapped_column(Date, nullable=False, index=True)
    market_regime: Mapped[str] = mapped_column(String(64))
    risk_level: Mapped[str] = mapped_column(String(32))
    turnover_trend: Mapped[str] = mapped_column(String(64))
    northbound_flow: Mapped[str] = mapped_column(String(64))
    trend_fit: Mapped[str] = mapped_column(String(64))
    recommended_exposure: Mapped[float] = mapped_column(Float)
    summary: Mapped[str] = mapped_column(Text)
    risk_note: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class SectorDaily(Base):
    __tablename__ = "sector_daily"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    date: Mapped[date] = mapped_column(Date, nullable=False, index=True)
    sector: Mapped[str] = mapped_column(String(128))
    sector_strength: Mapped[float] = mapped_column(Float)
    cycle_stage: Mapped[str] = mapped_column(String(64))
    vs_hs300: Mapped[float] = mapped_column(Float)
    flow_state: Mapped[str] = mapped_column(String(64))
    focus: Mapped[str] = mapped_column(String(128))
    one_liner: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class StockScanner(Base):
    __tablename__ = "stock_scanner"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    date: Mapped[date] = mapped_column(Date, nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(64))
    ticker: Mapped[str] = mapped_column(String(16), index=True)
    exchange: Mapped[str] = mapped_column(String(16))
    sector: Mapped[str] = mapped_column(String(64))
    price: Mapped[float] = mapped_column(Float)
    trend_score: Mapped[float] = mapped_column(Float)
    rs_score: Mapped[float] = mapped_column(Float)
    flow_score: Mapped[float] = mapped_column(Float)
    expectation_gap: Mapped[float] = mapped_column(Float)
    crowding: Mapped[float] = mapped_column(Float)
    risk_score: Mapped[float] = mapped_column(Float)
    total_score: Mapped[float] = mapped_column(Float)
    signal_type: Mapped[str] = mapped_column(String(64))
    entry_zone: Mapped[str] = mapped_column(String(128))
    stop_loss: Mapped[str] = mapped_column(String(128))
    trend_break: Mapped[str] = mapped_column(String(128))
    one_liner: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class TradePlan(Base):
    __tablename__ = "trade_plan"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    date: Mapped[date] = mapped_column(Date, nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(64))
    ticker: Mapped[str] = mapped_column(String(16))
    account: Mapped[str] = mapped_column(String(32))
    action: Mapped[str] = mapped_column(String(32))
    priority: Mapped[int] = mapped_column(Integer)
    planned_position_pct: Mapped[float] = mapped_column(Float)
    entry_condition: Mapped[str] = mapped_column(Text)
    entry_zone: Mapped[str] = mapped_column(String(128))
    stop_loss: Mapped[str] = mapped_column(String(128))
    take_profit_rule: Mapped[str] = mapped_column(Text)
    trend_break: Mapped[str] = mapped_column(String(128))
    notes: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class PortfolioRisk(Base):
    __tablename__ = "portfolio_risk"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    date: Mapped[date] = mapped_column(Date, nullable=False, index=True)
    accounta_exposure: Mapped[float] = mapped_column(Float)
    accountb_exposure: Mapped[float] = mapped_column(Float)
    max_single_position_pct: Mapped[float] = mapped_column(Float)
    top3_sector_concentration: Mapped[float] = mapped_column(Float)
    drawdown_today_pct: Mapped[float] = mapped_column(Float)
    drawdown_month_pct: Mapped[float] = mapped_column(Float)
    drawdown_year_pct: Mapped[float] = mapped_column(Float)
    loss_streak: Mapped[int] = mapped_column(Integer)
    risk_level: Mapped[str] = mapped_column(String(32))
    action_suggestion: Mapped[str] = mapped_column(Text)
    reason: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class TradeLog(Base):
    __tablename__ = "trade_log"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    date: Mapped[date] = mapped_column(Date, nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(64))
    ticker: Mapped[str] = mapped_column(String(16))
    account: Mapped[str] = mapped_column(String(32))
    side: Mapped[str] = mapped_column(String(8))
    price: Mapped[float] = mapped_column(Float)
    position_pct: Mapped[float] = mapped_column(Float)
    result: Mapped[str] = mapped_column(String(32))
    rule_trigger: Mapped[str] = mapped_column(Text)
    notes: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class Review(Base):
    __tablename__ = "review"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    date: Mapped[date] = mapped_column(Date, nullable=False, index=True)
    plan_adherence: Mapped[str] = mapped_column(String(64))
    good: Mapped[str] = mapped_column(Text)
    bad: Mapped[str] = mapped_column(Text)
    fixes: Mapped[str] = mapped_column(Text)
    tomorrow_focus: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

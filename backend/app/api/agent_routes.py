from fastapi import APIRouter

from app.agents.agents import (
    macro_analyst_ai,
    market_scanner_ai,
    money_flow_ai,
    review_ai,
    risk_control_ai,
    sector_analyst_ai,
    stock_research_ai,
    trade_strategy_ai,
)

router = APIRouter(prefix="/api/agents", tags=["agents"])


@router.get("/macro")
def macro_agent():
    return macro_analyst_ai()


@router.get("/sector")
def sector_agent():
    return sector_analyst_ai()


@router.get("/scanner")
def scanner_agent():
    return market_scanner_ai()


@router.get("/research")
def research_agent():
    return stock_research_ai()


@router.get("/flow")
def flow_agent():
    return money_flow_ai()


@router.get("/strategy")
def strategy_agent():
    return trade_strategy_ai()


@router.get("/risk")
def risk_agent():
    return risk_control_ai()


@router.get("/review")
def review_agent():
    return review_ai()

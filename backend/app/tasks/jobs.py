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
from app.tasks.celery_app import celery_app


@celery_app.task
def run_macro_and_sector():
    return {"macro": macro_analyst_ai(), "sector": sector_analyst_ai()}


@celery_app.task
def run_market_scanner():
    return market_scanner_ai()


@celery_app.task
def run_stock_research():
    return stock_research_ai()


@celery_app.task
def run_money_flow():
    return money_flow_ai()


@celery_app.task
def run_trade_strategy():
    return trade_strategy_ai()


@celery_app.task
def run_risk_control():
    return risk_control_ai()


@celery_app.task
def run_review():
    return review_ai()

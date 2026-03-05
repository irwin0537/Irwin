from celery import Celery
from celery.schedules import crontab

from app.core.config import settings

celery_app = Celery("ai_trading_os", broker=settings.redis_url, backend=settings.redis_url)

celery_app.conf.timezone = "Asia/Shanghai"
celery_app.conf.beat_schedule = {
    "0830-macro-sector": {
        "task": "app.tasks.jobs.run_macro_and_sector",
        "schedule": crontab(hour=8, minute=30),
    },
    "0910-scanner": {
        "task": "app.tasks.jobs.run_market_scanner",
        "schedule": crontab(hour=9, minute=10),
    },
    "1030-stock-research": {
        "task": "app.tasks.jobs.run_stock_research",
        "schedule": crontab(hour=10, minute=30),
    },
    "1330-money-flow": {
        "task": "app.tasks.jobs.run_money_flow",
        "schedule": crontab(hour=13, minute=30),
    },
    "1430-trade-strategy": {
        "task": "app.tasks.jobs.run_trade_strategy",
        "schedule": crontab(hour=14, minute=30),
    },
    "1530-risk-control": {
        "task": "app.tasks.jobs.run_risk_control",
        "schedule": crontab(hour=15, minute=30),
    },
    "2030-review": {
        "task": "app.tasks.jobs.run_review",
        "schedule": crontab(hour=20, minute=30),
    },
}

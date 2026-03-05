from datetime import date

from sqlalchemy import desc
from sqlalchemy.orm import Session

from app.models.entities import MarketDaily, PortfolioRisk, Review, SectorDaily, StockScanner, TradePlan


def get_latest_market(db: Session):
    return db.query(MarketDaily).order_by(desc(MarketDaily.date)).first()


def get_latest_sectors(db: Session):
    return db.query(SectorDaily).order_by(desc(SectorDaily.sector_strength)).limit(10).all()


def get_latest_scanner(db: Session):
    return db.query(StockScanner).order_by(desc(StockScanner.total_score)).limit(20).all()


def get_latest_trade_plan(db: Session):
    return db.query(TradePlan).order_by(desc(TradePlan.priority)).limit(10).all()


def get_latest_risk(db: Session):
    return db.query(PortfolioRisk).order_by(desc(PortfolioRisk.date)).first()


def get_latest_review(db: Session):
    return db.query(Review).order_by(desc(Review.date)).first()


def seed_demo_data(db: Session):
    if get_latest_market(db):
        return

    today = date.today()
    db.add(
        MarketDaily(
            date=today,
            market_regime="Risk-On",
            risk_level="Medium",
            turnover_trend="Rising",
            northbound_flow="Net Inflow",
            trend_fit="Momentum",
            recommended_exposure=62.0,
            summary="指数延续上行，科技成长与高股息轮动。",
            risk_note="警惕高位拥挤板块的日内波动。",
        )
    )

    for idx, sector in enumerate(["AI", "Semiconductor", "Brokerage", "Power Grid", "Auto"]):
        db.add(
            SectorDaily(
                date=today,
                sector=sector,
                sector_strength=90 - idx * 6,
                cycle_stage="Expansion",
                vs_hs300=2.5 - idx * 0.3,
                flow_state="Strong Inflow",
                focus=f"{sector} 龙头",
                one_liner=f"{sector} 资金持续净流入。",
            )
        )

    db.add(
        StockScanner(
            date=today,
            name="NVIDIA",
            ticker="NVDA",
            exchange="NASDAQ",
            sector="AI",
            price=1023.5,
            trend_score=92,
            rs_score=90,
            flow_score=88,
            expectation_gap=70,
            crowding=65,
            risk_score=40,
            total_score=89,
            signal_type="Breakout",
            entry_zone="1000-1015",
            stop_loss="980",
            trend_break="5D MA",
            one_liner="业绩与资金共振。",
        )
    )

    db.add(
        TradePlan(
            date=today,
            name="NVIDIA",
            ticker="NVDA",
            account="AccountA",
            action="Buy",
            priority=1,
            planned_position_pct=12,
            entry_condition="开盘后30分钟站稳VWAP",
            entry_zone="1000-1015",
            stop_loss="980",
            take_profit_rule="分批止盈：+8%/+15%",
            trend_break="跌破5日线减半",
            notes="若盘中放量长上影，降低仓位。",
        )
    )

    db.add(
        PortfolioRisk(
            date=today,
            accounta_exposure=58,
            accountb_exposure=42,
            max_single_position_pct=15,
            top3_sector_concentration=49,
            drawdown_today_pct=0.8,
            drawdown_month_pct=3.1,
            drawdown_year_pct=5.4,
            loss_streak=1,
            risk_level="Medium",
            action_suggestion="总仓位可维持在60%附近，控制单票回撤。",
            reason="组合集中度可控，但成长板块波动上升。",
        )
    )

    db.add(
        Review(
            date=today,
            plan_adherence="85%",
            good="严格执行止损与分批止盈。",
            bad="午后追高一次。",
            fixes="仅在二次确认后加仓。",
            tomorrow_focus="观察AI链条分歧后的回流强度。",
        )
    )
    db.commit()

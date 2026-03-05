CREATE TABLE IF NOT EXISTS market_daily (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    market_regime VARCHAR(64),
    risk_level VARCHAR(32),
    turnover_trend VARCHAR(64),
    northbound_flow VARCHAR(64),
    trend_fit VARCHAR(64),
    recommended_exposure FLOAT,
    summary TEXT,
    risk_note TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS sector_daily (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    sector VARCHAR(128),
    sector_strength FLOAT,
    cycle_stage VARCHAR(64),
    vs_hs300 FLOAT,
    flow_state VARCHAR(64),
    focus VARCHAR(128),
    one_liner TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS stock_scanner (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    name VARCHAR(64),
    ticker VARCHAR(16),
    exchange VARCHAR(16),
    sector VARCHAR(64),
    price FLOAT,
    trend_score FLOAT,
    rs_score FLOAT,
    flow_score FLOAT,
    expectation_gap FLOAT,
    crowding FLOAT,
    risk_score FLOAT,
    total_score FLOAT,
    signal_type VARCHAR(64),
    entry_zone VARCHAR(128),
    stop_loss VARCHAR(128),
    trend_break VARCHAR(128),
    one_liner TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS trade_plan (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    name VARCHAR(64),
    ticker VARCHAR(16),
    account VARCHAR(32),
    action VARCHAR(32),
    priority INTEGER,
    planned_position_pct FLOAT,
    entry_condition TEXT,
    entry_zone VARCHAR(128),
    stop_loss VARCHAR(128),
    take_profit_rule TEXT,
    trend_break VARCHAR(128),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS portfolio_risk (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    accounta_exposure FLOAT,
    accountb_exposure FLOAT,
    max_single_position_pct FLOAT,
    top3_sector_concentration FLOAT,
    drawdown_today_pct FLOAT,
    drawdown_month_pct FLOAT,
    drawdown_year_pct FLOAT,
    loss_streak INTEGER,
    risk_level VARCHAR(32),
    action_suggestion TEXT,
    reason TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS trade_log (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    name VARCHAR(64),
    ticker VARCHAR(16),
    account VARCHAR(32),
    side VARCHAR(8),
    price FLOAT,
    position_pct FLOAT,
    result VARCHAR(32),
    rule_trigger TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS review (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    plan_adherence VARCHAR(64),
    good TEXT,
    bad TEXT,
    fixes TEXT,
    tomorrow_focus TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

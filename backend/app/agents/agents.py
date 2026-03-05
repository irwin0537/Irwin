from datetime import datetime


def _agent_output(agent_name: str, topic: str):
    return {
        "agent": agent_name,
        "topic": topic,
        "timestamp": datetime.utcnow().isoformat(),
        "summary": f"{agent_name} completed analysis for {topic}.",
        "status": "ok",
    }


def macro_analyst_ai():
    return _agent_output("Macro Analyst AI", "market regime")


def sector_analyst_ai():
    return _agent_output("Sector Analyst AI", "sector heatmap")


def market_scanner_ai():
    return _agent_output("Market Scanner AI", "candidate universe")


def stock_research_ai():
    return _agent_output("Stock Research AI", "deep stock review")


def money_flow_ai():
    return _agent_output("Money Flow AI", "capital flow")


def trade_strategy_ai():
    return _agent_output("Trade Strategy AI", "trade plan")


def risk_control_ai():
    return _agent_output("Risk Control AI", "portfolio risk")


def review_ai():
    return _agent_output("Review AI", "daily review")

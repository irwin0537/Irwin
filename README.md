# AI Trading OS

AI 驱动交易研究平台（Notion + TradingView + Hedge Fund Dashboard 风格）。

## 项目结构

- `frontend/`：Next.js 可视化交易控制台
- `backend/`：FastAPI + SQLAlchemy API 服务
- `database/`：PostgreSQL 初始化脚本
- `backend/app/agents/`：8 个 AI 员工接口
- `backend/app/tasks/`：Celery 定时任务（对应每日执行时间）

## 功能覆盖

- 6 大模块页面：Dashboard / Sector Map / Stock Scanner / Trade Planner / Portfolio Risk / Review
- 7 张核心数据库表
- API：
  - `/api/market`
  - `/api/sectors`
  - `/api/scanner`
  - `/api/trade-plan`
  - `/api/risk`
  - `/api/review`
- AI Agent API：`/api/agents/*`
- 自动调度：Celery worker + Celery beat

## 一键启动

```bash
docker-compose up --build
```

启动后访问：

- 前端：http://localhost:3000
- 后端文档：http://localhost:8000/docs

## 说明

- 后端启动时会自动建表并写入演示数据。
- Celery Beat 已按需求配置调度时间（08:30 ~ 20:30）。

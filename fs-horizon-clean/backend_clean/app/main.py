from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Literal

app = FastAPI(title="FS Horizon Radar API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Issue(BaseModel):
    id: str
    title: str
    theme: str
    geography: str
    credibility: Literal["high", "medium", "watch"]
    summary: str
    so_what: str

class DashboardSummary(BaseModel):
    themes: List[str]
    issues: List[Issue]

@app.get("/")
async def root():
    return {"message": "FS Horizon Radar backend is running"}

@app.get("/health")
async def health():
    return {"ok": True}

@app.get("/api/dashboard", response_model=DashboardSummary)
async def get_dashboard():
    issues = [
        Issue(
            id="geo-natsec-1",
            title="Geopolitical tension, national security and strategic dependency risks are rising",
            theme="Geopolitics & national security",
            geography="UK + global",
            credibility="high",
            summary="Cross-border disruption, sanctions shifts and supply chain concentration remain active strategic risks.",
            so_what="Review your top geopolitical dependencies this quarter and identify where you need backup suppliers or contingency plans."
        ),
        Issue(
            id="cyber-res-1",
            title="Cyber resilience and operational resilience are converging into a single supervisory concern",
            theme="Cyber & resilience",
            geography="UK",
            credibility="high",
            summary="Firms are increasingly expected to manage cyber disruption and operational disruption as one resilience challenge.",
            so_what="Run one joined-up test of cyber response, third-party failure and business continuity this quarter."
        ),
        Issue(
            id="ai-risk-1",
            title="AI governance is moving from experimentation to accountability",
            theme="AI & data governance",
            geography="UK + EU + global",
            credibility="medium",
            summary="Supervisory and internal expectations are shifting toward clearer oversight of model use, data quality and accountability.",
            so_what="List every live AI use case, assign an owner to each one, and confirm the controls around data and approvals."
        ),
        Issue(
            id="conduct-1",
            title="Consumer duty and conduct expectations are reshaping product governance",
            theme="Consumer & conduct",
            geography="UK",
            credibility="high",
            summary="Firms are under pressure to show fair value, strong oversight and evidence of good customer outcomes.",
            so_what="Check your highest-risk products first and confirm you can evidence fair value and good customer outcomes."
        ),
        Issue(
            id="liq-cap-1",
            title="Volatility can quickly reprice liquidity and capital assumptions",
            theme="Prudential risk",
            geography="UK + global",
            credibility="watch",
            summary="Market stress can quickly change funding conditions, hedging assumptions and management actions.",
            so_what="Refresh your stress scenarios and confirm what actions the business would take if liquidity tightened quickly."
        )
    ]

    themes = sorted(list({issue.theme for issue in issues}))
    return DashboardSummary(themes=themes, issues=issues)

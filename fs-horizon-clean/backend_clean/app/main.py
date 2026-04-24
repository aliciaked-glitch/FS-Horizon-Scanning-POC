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
            summary="Signals point to a stronger overlap between financial stability, sanctions exposure, supply chain stress and geopolitical disruption.",
            so_what="Leadership teams should monitor sanctions exposure, dependency risk and resilience assumptions more closely."
        ),
        Issue(
            id="cyber-res-1",
            title="Cyber resilience and operational resilience are converging into a single supervisory concern",
            theme="Cyber & resilience",
            geography="UK",
            credibility="high",
            summary="Operational disruption, third-party dependency and cyber preparedness are increasingly being treated together by firms and supervisors.",
            so_what="Firms should test incident response, vendor risk and continuity plans as one joined-up resilience capability."
        ),
        Issue(
            id="ai-risk-1",
            title="AI governance is moving from experimentation to accountability",
            theme="AI & data governance",
            geography="UK + EU + global",
            credibility="medium",
            summary="The direction of travel is toward stronger controls around model use, explainability, accountability and data quality.",
            so_what="Businesses should maintain a clear inventory of AI use cases, owners, controls and escalation routes."
        ),
        Issue(
            id="conduct-1",
            title="Consumer duty and conduct expectations are reshaping product governance",
            theme="Consumer & conduct",
            geography="UK",
            credibility="high",
            summary="Firms face more pressure to evidence fair value, good outcomes and effective oversight over product design and distribution.",
            so_what="Product, compliance and distribution teams should use clearer MI and stronger governance around customer outcomes."
        ),
        Issue(
            id="liq-cap-1",
            title="Volatility can quickly reprice liquidity and capital assumptions",
            theme="Prudential risk",
            geography="UK + global",
            credibility="watch",
            summary="Stress events continue to show how quickly market shifts can affect funding, hedging and portfolio assumptions.",
            so_what="Treasury and risk teams should revisit scenario design and management actions under severe but plausible stress."
        )
    ]

    themes = sorted(list({issue.theme for issue in issues}))
    return DashboardSummary(themes=themes, issues=issues)

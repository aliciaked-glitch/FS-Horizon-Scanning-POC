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

class SourceItem(BaseModel):
    title: str
    publisher: str
    source_type: Literal["regulator", "news", "trade press", "social", "internal"]
    url: str
    credibility: Literal["high", "medium", "watch"]
    rationale: str

class Issue(BaseModel):
    id: str
    title: str
    theme: str
    geography: str
    credibility: Literal["high", "medium", "watch"]
    summary: str
    so_what: str
    origin_signal: str
    source_summary: str
    sources: List[SourceItem]

class DashboardSummary(BaseModel):
    themes: List[str]
    issues: List[Issue]

class FeedbackPayload(BaseModel):
    issue_id: str
    vote: Literal["up", "down"]

feedback_store: list[dict] = []

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
            so_what="Review your top geopolitical dependencies this quarter and identify where you need backup suppliers or contingency plans.",
            origin_signal="Driven mainly by regulator commentary and mainstream reporting on supply chain resilience and sanctions exposure.",
            source_summary="Primary signals come from official UK regulatory material and established news reporting, with low reliance on social media.",
            sources=[
                SourceItem(
                    title="Financial Stability Report",
                    publisher="Bank of England",
                    source_type="regulator",
                    url="https://www.bankofengland.co.uk/financial-stability-report",
                    credibility="high",
                    rationale="Primary UK financial stability source with direct supervisory relevance."
                ),
                SourceItem(
                    title="Sanctions and financial crime guidance",
                    publisher="FCA",
                    source_type="regulator",
                    url="https://www.fca.org.uk/firms/financial-crime/sanctions",
                    credibility="high",
                    rationale="Direct conduct and control guidance for regulated firms."
                ),
                SourceItem(
                    title="Global economy and markets coverage",
                    publisher="Financial Times",
                    source_type="news",
                    url="https://www.ft.com/world",
                    credibility="high",
                    rationale="Established reporting used to track market and geopolitical developments."
                )
            ]
        ),
        Issue(
            id="cyber-res-1",
            title="Cyber resilience and operational resilience are converging into a single supervisory concern",
            theme="Cyber & resilience",
            geography="UK",
            credibility="high",
            summary="Firms are increasingly expected to manage cyber disruption and operational disruption as one resilience challenge.",
            so_what="Run one joined-up test of cyber response, third-party failure and business continuity this quarter.",
            origin_signal="Driven by UK regulatory resilience requirements and operational incident preparedness guidance.",
            source_summary="This trend is anchored in direct regulator publications, supported by specialist reporting rather than social signals.",
            sources=[
                SourceItem(
                    title="Operational resilience hub",
                    publisher="FCA",
                    source_type="regulator",
                    url="https://www.fca.org.uk/firms/operational-resilience",
                    credibility="high",
                    rationale="Primary UK source on firm obligations and resilience expectations."
                ),
                SourceItem(
                    title="Operational resilience policy and supervision",
                    publisher="Bank of England",
                    source_type="regulator",
                    url="https://www.bankofengland.co.uk/prudential-regulation/operational-resilience",
                    credibility="high",
                    rationale="Primary prudential source for resilience expectations."
                ),
                SourceItem(
                    title="Cyber security and operational resilience coverage",
                    publisher="The Banker",
                    source_type="trade press",
                    url="https://www.thebanker.com/",
                    credibility="medium",
                    rationale="Useful sector context, but secondary to regulator material."
                )
            ]
        ),
        Issue(
            id="ai-risk-1",
            title="AI governance is moving from experimentation to accountability",
            theme="AI & data governance",
            geography="UK + EU + global",
            credibility="medium",
            summary="Supervisory and internal expectations are shifting toward clearer oversight of model use, data quality and accountability.",
            so_what="List every live AI use case, assign an owner to each one, and confirm the controls around data and approvals.",
            origin_signal="Driven by emerging regulatory direction, policy discussion and mainstream reporting on enterprise AI controls.",
            source_summary="The signal mixes official material and credible news coverage, so it is important but still evolving.",
            sources=[
                SourceItem(
                    title="AI updates and publications",
                    publisher="ICO",
                    source_type="regulator",
                    url="https://ico.org.uk/about-the-ico/media-centre/ai-updates/",
                    credibility="high",
                    rationale="Direct UK governance perspective on AI and data use."
                ),
                SourceItem(
                    title="Artificial intelligence topic hub",
                    publisher="Financial Times",
                    source_type="news",
                    url="https://www.ft.com/artificial-intelligence",
                    credibility="high",
                    rationale="Established reporting on enterprise AI and policy direction."
                ),
                SourceItem(
                    title="AI governance updates",
                    publisher="World Economic Forum",
                    source_type="trade press",
                    url="https://www.weforum.org/agenda/archive/artificial-intelligence/",
                    credibility="medium",
                    rationale="Useful strategic context but not a direct regulator source."
                )
            ]
        ),
        Issue(
            id="conduct-1",
            title="Consumer duty and conduct expectations are reshaping product governance",
            theme="Consumer & conduct",
            geography="UK",
            credibility="high",
            summary="Firms are under pressure to show fair value, strong oversight and evidence of good customer outcomes.",
            so_what="Check your highest-risk products first and confirm you can evidence fair value and good customer outcomes.",
            origin_signal="Driven directly by FCA consumer duty material and supporting industry coverage.",
            source_summary="This is a high-confidence trend because it comes mainly from direct UK regulatory expectations.",
            sources=[
                SourceItem(
                    title="Consumer Duty hub",
                    publisher="FCA",
                    source_type="regulator",
                    url="https://www.fca.org.uk/firms/consumer-duty",
                    credibility="high",
                    rationale="Primary source for UK conduct expectations and implementation materials."
                ),
                SourceItem(
                    title="Consumer protection and conduct reporting",
                    publisher="BBC News Business",
                    source_type="news",
                    url="https://www.bbc.com/news/business",
                    credibility="high",
                    rationale="Broad public reporting that can highlight customer-impact developments."
                ),
                SourceItem(
                    title="UK retail banking conduct coverage",
                    publisher="Financial Times",
                    source_type="news",
                    url="https://www.ft.com/companies/financials",
                    credibility="high",
                    rationale="Established source for firm and market conduct developments."
                )
            ]
        ),
        Issue(
            id="liq-cap-1",
            title="Volatility can quickly reprice liquidity and capital assumptions",
            theme="Prudential risk",
            geography="UK + global",
            credibility="watch",
            summary="Market stress can quickly change funding conditions, hedging assumptions and management actions.",
            so_what="Refresh your stress scenarios and confirm what actions the business would take if liquidity tightened quickly.",
            origin_signal="Driven by market volatility, prudential commentary and financial press coverage rather than a single new rule.",
            source_summary="This is a watch item with credible backing, but the timing and severity depend on market conditions.",
            sources=[
                SourceItem(
                    title="Prudential regulation publications",
                    publisher="Bank of England",
                    source_type="regulator",
                    url="https://www.bankofengland.co.uk/prudential-regulation/publication",
                    credibility="high",
                    rationale="Primary source for prudential expectations and supervisory thinking."
                ),
                SourceItem(
                    title="Markets and banking coverage",
                    publisher="Reuters",
                    source_type="news",
                    url="https://www.reuters.com/markets/",
                    credibility="high",
                    rationale="Widely used market news source for fast-moving developments."
                ),
                SourceItem(
                    title="Bank risk analysis",
                    publisher="Risk.net",
                    source_type="trade press",
                    url="https://www.risk.net/",
                    credibility="medium",
                    rationale="Specialist context source for risk practitioners."
                )
            ]
        )
    ]

    themes = sorted(list({issue.theme for issue in issues}))
    return DashboardSummary(themes=themes, issues=issues)

@app.post("/api/feedback")
async def submit_feedback(payload: FeedbackPayload):
    feedback_store.append(payload.model_dump())
    return {"ok": True, "saved": payload.model_dump(), "count": len(feedback_store)}

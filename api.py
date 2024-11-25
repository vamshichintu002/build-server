from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Union, Optional
import json
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import uvicorn
import os
from supabase import create_client, Client
from dotenv import load_dotenv
import json
from datetime import datetime
import asyncio
import pprint

# Load environment variables
load_dotenv()

class FinancialInfo(BaseModel):
    name: str
    monthly_salary: float
    other_incomes: float
    initial_investment: float
    risk_tolerance: str
    investment_timeline: str
    financial_goals: List[str]

app = FastAPI(
    title="Investment Portfolio Advisor API",
    description="API for generating personalized investment portfolio recommendations for Indian investors",
    version="1.0.0"
)

@app.post("/submit-financial-info")
async def submit_financial_info(info: FinancialInfo):
    try:
        # Generate client profile
        client_profile = {
            "risk_profile": {
                "tolerance_level": info.risk_tolerance,
                "investment_horizon": info.investment_timeline,
                "risk_capacity": "Medium"
            },
            "investment_objectives": {
                "primary_goals": info.financial_goals,
                "target_return": "8-10% annual return",
                "constraints": ["Inflation", "Market volatility", "Changes in tax laws"]
            },
            "financial_situation": {
                "initial_investment": info.initial_investment,
                "investment_category": "Balanced Portfolio",
                "liquidity_needs": "Medium"
            },
            "investment_strategy": {
                "asset_allocation": {
                    "Equity Mutual Funds": "50%",
                    "Debt Mutual Funds": "30%",
                    "Gold ETFs": "10%",
                    "Real Estate Investment Trusts (REITs)": "10%"
                },
                "tax_planning": "Investment in Equity Linked Saving Scheme (ELSS) and utilization of ₹150,000 tax deduction under section 80C",
                "risk_management": "Portfolio diversification and periodic rebalancing"
            },
            "market_analysis": {
                "economic_outlook": "Positive with expected steady growth",
                "sector_preference": "Information Technology, Pharmaceuticals, FMCG",
                "impact_of_global_factors": "Moderate"
            }
        }

        # Generate portfolio recommendation
        portfolio_recommendation = {
            "portfolio": {
                "Large_Cap_Stocks": 25,
                "Mid_Cap_Stocks": 15,
                "Small_Cap_Stocks": 10,
                "Government_Bonds": 20,
                "Corporate_FDs": 10,
                "Mutual_Funds": 15,
                "Gold_ETFs": 5
            },
            "strategy": f"Based on the client's {info.risk_tolerance.lower()} risk profile and medium-term investment horizon of {info.investment_timeline}, a balanced portfolio strategy is adopted. 50% of the portfolio is allocated to equity through a combination of large-cap, mid-cap, and small-cap stocks. This will provide a good mix of stability and growth. Large-cap stocks provide stability, while mid-cap and small-cap stocks offer higher growth potential. Preference is given to sectors like IT, Pharmaceuticals, and FMCG as per the client's preference and the positive economic outlook. 30% of the portfolio is allocated to debt instruments including government bonds and corporate fixed deposits, ensuring regular income and safety of capital. The remaining 20% is invested in mutual funds and Gold ETFs for further diversification and hedge against inflation. Regular portfolio rebalancing and tax planning through ELSS investments are part of the strategy to manage risk and optimize returns."
        }

        # Generate market analysis
        market_analysis = {
            "market_trends": {
                "nifty50_outlook": "The Indian market has been on a strong uptrend, thanks to robust corporate earnings and positive economic indicators. However, rising inflation and interest rates could pose challenges.",
                "sector_analysis": {
                    "Reliance_Industries": "Reliance operates in sectors like telecom, retail, and oil & gas. While telecom and retail have shown robust growth, the oil sector faces global volatility.",
                    "TCS": "The IT sector is experiencing strong demand due to the digital transformation wave. However, wage inflation and attrition are concerns.",
                    "HDFCBANK": "The banking sector is recovering from the NPAs issue but rising interest rates could affect loan growth.",
                    "Infosys": "Similar to TCS, Infosys is part of the IT sector which is seeing robust demand but wage inflation and attrition are key issues.",
                    "Bharti_Airtel": "The telecom sector is seeing intense competition but data consumption growth is a positive factor."
                },
                "global_factors": ["US interest rate hikes", "Global oil prices", "Trade wars"]
            },
            "risk_analysis": {
                "market_risks": ["Rising inflation", "Interest rate hikes"],
                "regulatory_risks": ["Changes in corporate tax rates", "Regulatory changes in sectors like telecom and banking"],
                "company_specific_risks": {
                    "Reliance_Industries": ["High debt levels", "Competition in telecom sector"],
                    "TCS": ["Wage inflation", "Attrition"],
                    "HDFCBANK": ["Asset quality", "Loan growth"],
                    "Infosys": ["Wage inflation", "Attrition"],
                    "Bharti_Airtel": ["Competition", "Regulatory changes"]
                }
            },
            "growth_potential": {
                "short_term": {
                    "Reliance_Industries": "Positive due to telecom and retail growth",
                    "TCS": "Positive due to strong IT demand",
                    "HDFCBANK": "Neutral due to rising interest rates",
                    "Infosys": "Positive due to strong IT demand",
                    "Bharti_Airtel": "Neutral due to intense competition"
                },
                "long_term": {
                    "Reliance_Industries": "Positive due to diversification",
                    "TCS": "Positive due to digital transformation wave",
                    "HDFCBANK": "Positive due to expanding economy",
                    "Infosys": "Positive due to digital transformation wave",
                    "Bharti_Airtel": "Positive due to data consumption growth"
                },
                "catalysts": ["Lowering of corporate tax rates", "Stronger economic growth", "Digital transformation wave"]
            },
            "recommendations": {
                "buy_hold_sell": {
                    "Reliance_Industries": "BUY",
                    "TCS": "BUY",
                    "HDFCBANK": "HOLD",
                    "Infosys": "BUY",
                    "Bharti_Airtel": "HOLD"
                },
                "target_prices": {
                    "Reliance_Industries": "3200",
                    "TCS": "3500",
                    "HDFCBANK": "1650",
                    "Infosys": "1800",
                    "Bharti_Airtel": "750"
                },
                "investment_horizon": {
                    "Reliance_Industries": "long term",
                    "TCS": "long term",
                    "HDFCBANK": "medium term",
                    "Infosys": "long term",
                    "Bharti_Airtel": "medium term"
                }
            }
        }

        return {
            "client_profile": client_profile,
            "portfolio_recommendation": portfolio_recommendation,
            "market_analysis": market_analysis
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)

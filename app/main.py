from fastapi import FastAPI
from app.routes import churn, ltv, fraud, segmentation, engagement
from app.utils.logger import setup_logger

app = FastAPI(
    title="AI-Powered CRM Backend",
    description="FastAPI backend for CRM with ML predictions using Canada777 API",
    version="1.0.0"
)

logger = setup_logger()

app.include_router(churn.router, prefix="/churn", tags=["Churn Prediction"])
app.include_router(ltv.router, prefix="/ltv", tags=["LTV Prediction"])
app.include_router(fraud.router, prefix="/fraud", tags=["Fraud Detection"])
app.include_router(segmentation.router, prefix="/segmentation", tags=["Segmentation"])
app.include_router(engagement.router, prefix="/engagement", tags=["Engagement Prediction"])

@app.get("/")
async def root():
    return {"message": "Welcome to the AI-Powered CRM Backend"}





# from fastapi import FastAPI
# from app.routes import churn, fraud, segmentation, engagement

# app = FastAPI()

# app.include_router(churn.router, prefix="/churn", tags=["churn"])
# app.include_router(fraud.router, prefix="/fraud", tags=["fraud"])
# app.include_router(segmentation.router, prefix="/segmentation", tags=["segmentation"])
# app.include_router(engagement.router, prefix="/engagement", tags=["engagement"])

# @app.get("/")
# async def root():
#     return {"message": "Welcome to the Canada777 Prediction API"}

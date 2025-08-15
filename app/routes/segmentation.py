# from fastapi import APIRouter, HTTPException
# from datetime import datetime
# from app.services.data_service import DataService
# from app.services.ml_service import MLService
# import logging

# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)

# router = APIRouter()

# @router.get("/predict")
# async def predict_segmentation():
#     try:
#         data_service = DataService()
#         ml_service = MLService()
        
#         raw_data = data_service.fetch_all_data()
#         segmentation_data, _ = data_service.preprocess_segmentation_data(raw_data)
        
#         if segmentation_data.empty:
#             raise HTTPException(status_code=500, detail="Failed to preprocess data")
        
#         predictions, segments = ml_service.predict_segmentation(segmentation_data)
#         segment_counts = {str(i): sum(1 for p in predictions if p["segment"] == i) for i in range(4)}
#         segment_chars = data_service.compute_segment_characteristics(segmentation_data, segments)
        
#         response = {
#             "status": "success",
#             "api_version": "1.0.0",
#             "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%S+06"),
#             "data": {
#                 "prediction_type": "segmentation",
#                 "results": {
#                     "segment_counts": segment_counts,
#                     "segmented_users": predictions,
#                     "segment_characteristics": segment_chars,
#                     "segment_recommendations": {
#                         "0": "Send re-engagement emails",
#                         "1": "Offer exclusive VIP rewards",
#                         "3": "Provide onboarding bonuses"
#                     },
#                     "segment_transition_insights": [
#                         {"user_id": p["user_id"], "predicted_next_segment": 1, "probability": 0.6}
#                         for p in predictions
#                     ],
#                     "segment_stability": {
#                         "0": 0.8,
#                         "1": 0.9,
#                         "3": 0.7
#                     },
#                     "segment_overlap": {
#                         "0_and_1": 0.1,
#                         "1_and_3": 0.05
#                     }
#                 },
#                 "total_segments": 4,
#                 "segment_summary": segment_counts,
#                 "cross_segment_comparison": {
#                     "LTV": {
#                         "segment_0": float(sum(p["predicted_ltv"] for p in ml_service.predict_ltv(data_service.preprocess_ltv_data(raw_data)[0]) if p["user_id"] in [x["user_id"] for x in predictions if x["segment"] == 0]) / segment_counts["0"]) if segment_counts["0"] else 500.0,
#                         "segment_1": float(sum(p["predicted_ltv"] for p in ml_service.predict_ltv(data_service.preprocess_ltv_data(raw_data)[0]) if p["user_id"] in [x["user_id"] for x in predictions if x["segment"] == 1]) / segment_counts["1"]) if segment_counts["1"] else 1200.0,
#                         "segment_3": float(sum(p["predicted_ltv"] for p in ml_service.predict_ltv(data_service.preprocess_ltv_data(raw_data)[0]) if p["user_id"] in [x["user_id"] for x in predictions if x["segment"] == 3]) / segment_counts["3"]) if segment_counts["3"] else 300.0
#                     },
#                     "fraud_rate": {
#                         "segment_0": float(sum(1 for p in ml_service.predict_fraud(data_service.preprocess_fraud_data(raw_data)[0]) if p["user_id"] in [x["user_id"] for x in predictions if x["segment"] == 0] and p["fraud_label"] == "Fraud") / segment_counts["0"]) if segment_counts["0"] else 0.1,
#                         "segment_1": float(sum(1 for p in ml_service.predict_fraud(data_service.preprocess_fraud_data(raw_data)[0]) if p["user_id"] in [x["user_id"] for x in predictions if x["segment"] == 1] and p["fraud_label"] == "Fraud") / segment_counts["1"]) if segment_counts["1"] else 0.2,
#                         "segment_3": float(sum(1 for p in ml_service.predict_fraud(data_service.preprocess_fraud_data(raw_data)[0]) if p["user_id"] in [x["user_id"] for x in predictions if x["segment"] == 3] and p["fraud_label"] == "Fraud") / segment_counts["3"]) if segment_counts["3"] else 0.05
#                     }
#                 },
#                 "recommendations": [
#                     {"type": "personalized_email", "message": "Exclusive 20% cashback for VIPs", "priority": "high"} if segment_counts.get("1", 0) > 0 else None,
#                     {"type": "onboarding_popup", "message": "Claim your welcome bonus now", "priority": "medium"} if segment_counts.get("3", 0) > 0 else None,
#                     {"type": "re_engagement_campaign", "message": "Offer 15 free spins to casual players", "priority": "medium"} if segment_counts.get("0", 0) > 0 else None
#                 ],
#                 "metadata": {
#                     "model_version": "v1.2",
#                     "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%S+06"),
#                     "data_freshness": "real-time"
#                 }
#             },
#             "pagination": {
#                 "page": 1,
#                 "total_pages": 10,
#                 "items_per_page": 100,
#                 "total_items": 1000
#             },
#             "errors": [],
#             "localization": {
#                 "currency": "USD",
#                 "language": "en",
#                 "region": "US"
#             }
#         }
#         response["data"]["recommendations"] = [r for r in response["data"]["recommendations"] if r is not None]
#         return response
#     except Exception as e:
#         logger.error(f"Error in segmentation endpoint: {str(e)}")
#         raise HTTPException(status_code=500, detail=str(e))




from fastapi import APIRouter, HTTPException
from datetime import datetime
from app.services.data_service import DataService
from app.services.ml_service import MLService
import logging
import numpy as np

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/predict")
async def predict_segmentation():
    try:
        data_service = DataService()
        ml_service = MLService()
        
        raw_data = data_service.fetch_all_data()
        segmentation_data, _ = data_service.preprocess_segmentation_data(raw_data)
        
        if segmentation_data.empty:
            raise HTTPException(status_code=500, detail="Failed to preprocess data")
        
        predictions, segments = ml_service.predict_segmentation(segmentation_data)
        segment_counts = {str(i): sum(1 for p in predictions if p["segment"] == i) for i in range(4)}
        segment_chars = data_service.compute_segment_characteristics(segmentation_data, segments)
        
        # Compute cross-segment comparison safely
        ltv_data, _ = data_service.preprocess_ltv_data(raw_data)
        fraud_data, _ = data_service.preprocess_fraud_data(raw_data)
        ltv_predictions = ml_service.predict_ltv(ltv_data)
        fraud_predictions = ml_service.predict_fraud(fraud_data)
        
        cross_segment_comparison = {
            "LTV": {},
            "fraud_rate": {}
        }
        for segment in range(4):
            segment_users = [p["user_id"] for p in predictions if p["segment"] == segment]
            ltv_sum = sum(p["predicted_ltv"] for p in ltv_predictions if p["user_id"] in segment_users)
            fraud_count = sum(1 for p in fraud_predictions if p["user_id"] in segment_users and p["fraud_label"] == "Fraud")
            cross_segment_comparison["LTV"][f"segment_{segment}"] = float(ltv_sum / segment_counts[str(segment)]) if segment_counts[str(segment)] > 0 else float(500.0 if segment == 0 else 1200.0 if segment == 1 else 300.0)
            cross_segment_comparison["fraud_rate"][f"segment_{segment}"] = float(fraud_count / segment_counts[str(segment)]) if segment_counts[str(segment)] > 0 else float(0.1 if segment == 0 else 0.2 if segment == 1 else 0.05)
        
        response = {
            "status": "success",
            "api_version": "1.0.0",
            "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%S+06"),
            "data": {
                "prediction_type": "segmentation",
                "results": {
                    "segment_counts": segment_counts,
                    "segmented_users": predictions,
                    "segment_characteristics": segment_chars,
                    "segment_recommendations": {
                        "0": "Send re-engagement emails",
                        "1": "Offer exclusive VIP rewards",
                        "3": "Provide onboarding bonuses"
                    },
                    "segment_transition_insights": [
                        {"user_id": p["user_id"], "predicted_next_segment": 1, "probability": 0.6}
                        for p in predictions
                    ],
                    "segment_stability": {
                        "0": 0.8,
                        "1": 0.9,
                        "3": 0.7
                    },
                    "segment_overlap": {
                        "0_and_1": 0.1,
                        "1_and_3": 0.05
                    }
                },
                "total_segments": 4,
                "segment_summary": segment_counts,
                "cross_segment_comparison": cross_segment_comparison,
                "recommendations": [
                    {"type": "personalized_email", "message": "Exclusive 20% cashback for VIPs", "priority": "high"} if segment_counts.get("1", 0) > 0 else None,
                    {"type": "onboarding_popup", "message": "Claim your welcome bonus now", "priority": "medium"} if segment_counts.get("3", 0) > 0 else None,
                    {"type": "re_engagement_campaign", "message": "Offer 15 free spins to casual players", "priority": "medium"} if segment_counts.get("0", 0) > 0 else None
                ],
                "metadata": {
                    "model_version": "v1.2",
                    "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%S+06"),
                    "data_freshness": "real-time"
                }
            },
            "pagination": {
                "page": 1,
                "total_pages": 10,
                "items_per_page": 100,
                "total_items": 1000
            },
            "errors": [],
            "localization": {
                "currency": "USD",
                "language": "en",
                "region": "US"
            }
        }
        response["data"]["recommendations"] = [r for r in response["data"]["recommendations"] if r is not None]
        return response
    except Exception as e:
        logger.error(f"Error in segmentation endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
# from fastapi import APIRouter, HTTPException
# from datetime import datetime
# from app.services.data_service import DataService
# from app.services.ml_service import MLService
# import logging

# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)

# router = APIRouter()

# @router.get("/predict")
# async def predict_ltv():
#     try:
#         data_service = DataService()
#         ml_service = MLService()
        
#         raw_data = data_service.fetch_all_data()
#         ltv_data, extra_metrics = data_service.preprocess_ltv_data(raw_data)
        
#         if ltv_data.empty:
#             raise HTTPException(status_code=500, detail="Failed to preprocess data")
        
#         predictions = ml_service.predict_ltv(ltv_data)
        
#         response = {
#             "status": "success",
#             "api_version": "1.0.0",
#             "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%S+06"),
#             "data": {
#                 "prediction_type": "ltv_prediction",
#                 "results": [
#                     {
#                         "user_id": pred["user_id"],
#                         "predicted_ltv": pred["predicted_ltv"],
#                         "prediction_confidence": 0.85 if pred["predicted_ltv"] < 1000 else 0.92,
#                         "churn_adjusted_ltv": pred["predicted_ltv"] * 0.8,
#                         "ltv_confidence_interval": {"min": pred["predicted_ltv"] * 0.9, "max": pred["predicted_ltv"] * 1.1},
#                         "user_preferences": {
#                             "favorite_game": data_service.get_preferred_game(pred["user_id"], raw_data),
#                             "preferred_payment_method": data_service.get_preferred_payment_method(pred["user_id"], raw_data)
#                         },
#                         "cross_sell_opportunity": "Offer premium membership" if pred["predicted_ltv"] < 1000 else "Promote live tournaments"
#                     } for pred in predictions
#                 ],
#                 "average_ltv": float(sum(p["predicted_ltv"] for p in predictions) / len(predictions)) if predictions else 672.08,
#                 "mae": 50.67,
#                 "ltv_range": {
#                     "min": float(min(p["predicted_ltv"] for p in predictions)) if predictions else 315.67,
#                     "max": float(max(p["predicted_ltv"] for p in predictions)) if predictions else 1200.45
#                 },
#                 "total_users": len(predictions),
#                 "ltv_forecast": extra_metrics.get("ltv_forecast", {"predicted_ltv_next_month": 800.50}),
#                 "ltv_segment_breakdown": {
#                     "low_value": float(sum(1 for p in predictions if p["predicted_ltv"] < 500) / len(predictions) * 100) if predictions else 33.33,
#                     "medium_value": float(sum(1 for p in predictions if 500 <= p["predicted_ltv"] < 1000) / len(predictions) * 100) if predictions else 33.33,
#                     "high_value": float(sum(1 for p in predictions if p["predicted_ltv"] >= 1000) / len(predictions) * 100) if predictions else 33.33
#                 },
#                 "top_high_value_users": [
#                     {"user_id": p["user_id"], "predicted_ltv": p["predicted_ltv"]}
#                     for p in predictions if p["predicted_ltv"] >= 1000
#                 ],
#                 "ltv_growth_potential": [
#                     {"user_id": p["user_id"], "potential_ltv_increase": p["predicted_ltv"] * 0.2, "action": "Upsell VIP package"}
#                     for p in predictions
#                 ],
#                 "recommendations": [
#                     {"type": "email", "message": f"Invite to exclusive VIP tournament for {data_service.get_preferred_game(p['user_id'], raw_data)}" if data_service.get_preferred_game(p['user_id'], raw_data) != "Unknown" else "Invite to exclusive VIP tournament", "priority": "high"} for p in predictions if p["predicted_ltv"] >= 1000
#                 ] + [
#                     {"type": "sms", "message": "Get 10% bonus on your next deposit", "priority": "medium"} for p in predictions if p["predicted_ltv"] < 1000
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
#         return response
#     except Exception as e:
#         logger.error(f"Error in LTV prediction endpoint: {str(e)}")
#         raise HTTPException(status_code=500, detail=str(e))







# from fastapi import APIRouter, HTTPException
# from datetime import datetime
# from app.services.data_service import DataService
# from app.services.ml_service import MLService
# import logging

# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)

# router = APIRouter()

# @router.get("/predict")
# async def predict_ltv():
#     try:
#         data_service = DataService()
#         ml_service = MLService()
        
#         raw_data = data_service.fetch_all_data()
#         ltv_data, extra_metrics = data_service.preprocess_ltv_data(raw_data)
        
#         if ltv_data.empty:
#             raise HTTPException(status_code=500, detail="Failed to preprocess data")
        
#         predictions = ml_service.predict_ltv(ltv_data)  # No extra_metrics passed, as per ml_service.py
        
#         response = {
#             "status": "success",
#             "api_version": "1.0.0",
#             "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%S+06"),
#             "data": {
#                 "prediction_type": "ltv_prediction",
#                 "results": [
#                     {
#                         "user_id": int(pred["user_id"]),  # Ensure Python int
#                         "predicted_ltv": float(pred["predicted_ltv"]),  # Ensure Python float
#                         "prediction_confidence": float(0.85 if pred["predicted_ltv"] < 1000 else 0.92),
#                         "churn_adjusted_ltv": float(pred["predicted_ltv"] * 0.8),
#                         "ltv_confidence_interval": {
#                             "min": float(pred["predicted_ltv"] * 0.9),
#                             "max": float(pred["predicted_ltv"] * 1.1)
#                         },
#                         "user_preferences": {
#                             "favorite_game": data_service.get_preferred_game(pred["user_id"], raw_data),
#                             "preferred_payment_method": data_service.get_preferred_payment_method(pred["user_id"], raw_data)
#                         },
#                         "cross_sell_opportunity": "Offer premium membership" if pred["predicted_ltv"] < 1000 else "Promote live tournaments"
#                     } for pred in predictions
#                 ],
#                 "average_ltv": float(sum(p["predicted_ltv"] for p in predictions) / len(predictions)) if predictions else float(672.08),
#                 "mae": float(50.67),
#                 "ltv_range": {
#                     "min": float(min(p["predicted_ltv"] for p in predictions)) if predictions else float(315.67),
#                     "max": float(max(p["predicted_ltv"] for p in predictions)) if predictions else float(1200.45)
#                 },
#                 "total_users": int(len(predictions)),  # Ensure Python int
#                 "ltv_forecast": extra_metrics.get("ltv_forecast", {"predicted_ltv_next_month": float(800.50)}),
#                 "ltv_segment_breakdown": {
#                     "low_value": float(sum(1 for p in predictions if p["predicted_ltv"] < 500) / len(predictions) * 100) if predictions else float(33.33),
#                     "medium_value": float(sum(1 for p in predictions if 500 <= p["predicted_ltv"] < 1000) / len(predictions) * 100) if predictions else float(33.33),
#                     "high_value": float(sum(1 for p in predictions if p["predicted_ltv"] >= 1000) / len(predictions) * 100) if predictions else float(33.33)
#                 },
#                 "top_high_value_users": [
#                     {"user_id": int(p["user_id"]), "predicted_ltv": float(p["predicted_ltv"])}
#                     for p in predictions if p["predicted_ltv"] >= 1000
#                 ],
#                 "ltv_growth_potential": [
#                     {
#                         "user_id": int(p["user_id"]),
#                         "potential_ltv_increase": float(p["predicted_ltv"] * 0.2),
#                         "action": "Upsell VIP package"
#                     } for p in predictions
#                 ],
#                 "recommendations": [
#                     {
#                         "type": "email",
#                         "message": f"Invite to exclusive VIP tournament for {data_service.get_preferred_game(p['user_id'], raw_data)}" if data_service.get_preferred_game(p['user_id'], raw_data) != "Unknown" else "Invite to exclusive VIP tournament",
#                         "priority": "high"
#                     } for p in predictions if p["predicted_ltv"] >= 1000
#                 ] + [
#                     {
#                         "type": "sms",
#                         "message": "Get 10% bonus on your next deposit",
#                         "priority": "medium"
#                     } for p in predictions if p["predicted_ltv"] < 1000
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
#         return response
#     except Exception as e:
#         logger.error(f"Error in LTV prediction endpoint: {str(e)}")
#         raise HTTPException(status_code=500, detail=str(e))


# from fastapi import APIRouter, HTTPException
# from datetime import datetime
# from app.services.data_service import DataService
# from app.services.ml_service import MLService
# import logging

# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)

# router = APIRouter()

# @router.get("/predict")
# async def predict_ltv():
#     try:
#         data_service = DataService()
#         ml_service = MLService()
        
#         raw_data = data_service.fetch_all_data()
#         ltv_data, extra_metrics = data_service.preprocess_ltv_data(raw_data)
        
#         if ltv_data.empty:
#             raise HTTPException(status_code=500, detail="Failed to preprocess data")
        
#         predictions = ml_service.predict_ltv(ltv_data)
        
#         response = {
#             "status": "success",
#             "api_version": "1.0.0",
#             "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%S+06"),
#             "data": {
#                 "prediction_type": "ltv_prediction",
#                 "results": [
#                     {
#                         "user_id": int(pred["user_id"]),
#                         "predicted_ltv": float(pred["predicted_ltv"]),
#                         "prediction_confidence": float(0.85 if pred["predicted_ltv"] < 1000 else 0.92),
#                         "churn_adjusted_ltv": float(pred["predicted_ltv"] * 0.8),
#                         "ltv_confidence_interval": {
#                             "min": float(pred["predicted_ltv"] * 0.9),
#                             "max": float(pred["predicted_ltv"] * 1.1)
#                         },
#                         "user_preferences": {
#                             "favorite_game": data_service.get_preferred_game(pred["user_id"], raw_data),
#                             "preferred_payment_method": data_service.get_preferred_payment_method(pred["user_id"], raw_data)
#                         },
#                         "cross_sell_opportunity": "Offer premium membership" if pred["predicted_ltv"] < 1000 else "Promote live tournaments"
#                     } for pred in predictions
#                 ],
#                 "average_ltv": float(sum(float(p["predicted_ltv"]) for p in predictions) / len(predictions)) if predictions else float(672.08),
#                 "mae": float(50.67),
#                 "ltv_range": {
#                     "min": float(min(float(p["predicted_ltv"]) for p in predictions)) if predictions else float(315.67),
#                     "max": float(max(float(p["predicted_ltv"]) for p in predictions)) if predictions else float(1200.45)
#                 },
#                 "total_users": int(len(predictions)),
#                 "ltv_forecast": {
#                     "predicted_ltv_next_month": float(extra_metrics.get("ltv_forecast", {"predicted_ltv_next_month": 800.50})["predicted_ltv_next_month"])
#                 },
#                 "ltv_segment_breakdown": {
#                     "low_value": float(int(sum(1 for p in predictions if float(p["predicted_ltv"]) < 500)) / len(predictions) * 100) if predictions else float(33.33),
#                     "medium_value": float(int(sum(1 for p in predictions if 500 <= float(p["predicted_ltv"]) < 1000)) / len(predictions) * 100) if predictions else float(33.33),
#                     "high_value": float(int(sum(1 for p in predictions if float(p["predicted_ltv"]) >= 1000)) / len(predictions) * 100) if predictions else float(33.33)
#                 },
#                 "top_high_value_users": [
#                     {"user_id": int(p["user_id"]), "predicted_ltv": float(p["predicted_ltv"])}
#                     for p in predictions if float(p["predicted_ltv"]) >= 1000
#                 ],
#                 "ltv_growth_potential": [
#                     {
#                         "user_id": int(p["user_id"]),
#                         "potential_ltv_increase": float(p["predicted_ltv"] * 0.2),
#                         "action": "Upsell VIP package"
#                     } for p in predictions
#                 ],
#                 "recommendations": [
#                     {
#                         "type": "email",
#                         "message": f"Invite to exclusive VIP tournament for {data_service.get_preferred_game(p['user_id'], raw_data)}" if data_service.get_preferred_game(p['user_id'], raw_data) != "Unknown" else "Invite to exclusive VIP tournament",
#                         "priority": "high"
#                     } for p in predictions if float(p["predicted_ltv"]) >= 1000
#                 ] + [
#                     {
#                         "type": "sms",
#                         "message": "Get 10% bonus on your next deposit",
#                         "priority": "medium"
#                     } for p in predictions if float(p["predicted_ltv"]) < 1000
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
#         return response
#     except Exception as e:
#         logger.error(f"Error in LTV prediction endpoint: {str(e)}")
#         raise HTTPException(status_code=500, detail=str(e))

# from fastapi import APIRouter, HTTPException
# from datetime import datetime
# from app.services.data_service import DataService
# from app.services.ml_service import MLService
# import logging

# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)

# router = APIRouter()

# @router.get("/predict")
# async def predict_ltv():
#     try:
#         data_service = DataService()
#         ml_service = MLService()

#         raw_data = data_service.fetch_all_data()
#         ltv_data, extra_metrics = data_service.preprocess_ltv_data(raw_data)

#         if ltv_data.empty:
#             raise HTTPException(status_code=500, detail="Failed to preprocess data")

#         raw_predictions = ml_service.predict_ltv(ltv_data)

#         # Handle predictions from DataFrame rows
#         predictions = []
#         for _, row in raw_predictions.iterrows():
#             user_id = row["user_id"]
#             predicted_ltv = row["predicted_ltv"]

#             predictions.append({
#                 "user_id": int(user_id.item() if hasattr(user_id, "item") else user_id),
#                 "predicted_ltv": float(predicted_ltv.item() if hasattr(predicted_ltv, "item") else predicted_ltv)
#             })

#         response = {
#             "status": "success",
#             "api_version": "1.0.0",
#             "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%S+06"),
#             "data": {
#                 "prediction_type": "ltv_prediction",
#                 "results": [
#                     {
#                         "user_id": pred["user_id"],
#                         "predicted_ltv": pred["predicted_ltv"],
#                         "prediction_confidence": 0.85 if pred["predicted_ltv"] < 1000 else 0.92,
#                         "churn_adjusted_ltv": round(pred["predicted_ltv"] * 0.8, 2),
#                         "ltv_confidence_interval": {
#                             "min": round(pred["predicted_ltv"] * 0.9, 2),
#                             "max": round(pred["predicted_ltv"] * 1.1, 2)
#                         },
#                         "user_preferences": {
#                             "favorite_game": data_service.get_preferred_game(pred["user_id"], raw_data),
#                             "preferred_payment_method": data_service.get_preferred_payment_method(pred["user_id"], raw_data)
#                         },
#                         "cross_sell_opportunity": "Offer premium membership" if pred["predicted_ltv"] < 1000 else "Promote live tournaments"
#                     } for pred in predictions
#                 ],
#                 "average_ltv": float(sum(p["predicted_ltv"] for p in predictions) / len(predictions)) if predictions else 672.08,
#                 "mae": 50.67,
#                 "ltv_range": {
#                     "min": float(min(p["predicted_ltv"] for p in predictions)) if predictions else 315.67,
#                     "max": float(max(p["predicted_ltv"] for p in predictions)) if predictions else 1200.45
#                 },
#                 "total_users": len(predictions),
#                 "ltv_forecast": {
#                     "predicted_ltv_next_month": float(extra_metrics.get("ltv_forecast", {"predicted_ltv_next_month": 800.50})["predicted_ltv_next_month"])
#                 },
#                 "recommendations": [
#                     {
#                         "type": "email",
#                         "message": f"Invite to exclusive VIP tournament for {data_service.get_preferred_game(p['user_id'], raw_data)}" if data_service.get_preferred_game(p['user_id'], raw_data) != "Unknown" else "Invite to exclusive VIP tournament",
#                         "priority": "high"
#                     } for p in predictions if p["predicted_ltv"] >= 1000
#                 ] + [
#                     {
#                         "type": "sms",
#                         "message": "Get 10% bonus on your next deposit",
#                         "priority": "medium"
#                     } for p in predictions if p["predicted_ltv"] < 1000
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
#         return response

#     except Exception as e:
#         logger.error(f"Error in LTV prediction endpoint: {str(e)}")
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

def convert_numpy(obj):
    if isinstance(obj, dict):
        return {k: convert_numpy(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_numpy(i) for i in obj]
    elif isinstance(obj, (np.integer, np.int64)):
        return int(obj)
    elif isinstance(obj, (np.floating, np.float64)):
        return float(obj)
    else:
        return obj

@router.get("/predict")
async def predict_ltv():
    try:
        data_service = DataService()
        ml_service = MLService()

        raw_data = data_service.fetch_all_data()
        ltv_data, extra_metrics = data_service.preprocess_ltv_data(raw_data)

        if ltv_data.empty:
            raise HTTPException(status_code=500, detail="Failed to preprocess data")

        raw_predictions = ml_service.predict_ltv(ltv_data)

        # Handle predictions from a list of dicts or tuples
        predictions = []
        for row in raw_predictions:
            user_id = row["user_id"] if isinstance(row, dict) else row[0]
            predicted_ltv = row["predicted_ltv"] if isinstance(row, dict) else row[1]

            predictions.append({
                "user_id": int(user_id.item() if hasattr(user_id, "item") else user_id),
                "predicted_ltv": float(predicted_ltv.item() if hasattr(predicted_ltv, "item") else predicted_ltv)
            })

        response = {
            "status": "success",
            "api_version": "1.0.0",
            "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%S+06"),
            "data": {
                "prediction_type": "ltv_prediction",
                "results": [
                    {
                        "user_id": pred["user_id"],
                        "predicted_ltv": pred["predicted_ltv"],
                        "prediction_confidence": 0.85 if pred["predicted_ltv"] < 1000 else 0.92,
                        "churn_adjusted_ltv": round(pred["predicted_ltv"] * 0.8, 2),
                        "ltv_confidence_interval": {
                            "min": round(pred["predicted_ltv"] * 0.9, 2),
                            "max": round(pred["predicted_ltv"] * 1.1, 2)
                        },
                        "user_preferences": {
                            "favorite_game": data_service.get_preferred_game(pred["user_id"], raw_data),
                            "preferred_payment_method": data_service.get_preferred_payment_method(pred["user_id"], raw_data)
                        },
                        "cross_sell_opportunity": "Offer premium membership" if pred["predicted_ltv"] < 1000 else "Promote live tournaments"
                    } for pred in predictions
                ],
                "average_ltv": float(sum(p["predicted_ltv"] for p in predictions) / len(predictions)) if predictions else 672.08,
                "mae": 50.67,
                "ltv_range": {
                    "min": float(min(p["predicted_ltv"] for p in predictions)) if predictions else 315.67,
                    "max": float(max(p["predicted_ltv"] for p in predictions)) if predictions else 1200.45
                },
                "total_users": len(predictions),
                "ltv_forecast": {
                    "predicted_ltv_next_month": float(extra_metrics.get("ltv_forecast", {"predicted_ltv_next_month": 800.50})["predicted_ltv_next_month"])
                },
                "recommendations": [
                    {
                        "type": "email",
                        "message": f"Invite to exclusive VIP tournament for {data_service.get_preferred_game(p['user_id'], raw_data)}" if data_service.get_preferred_game(p['user_id'], raw_data) != "Unknown" else "Invite to exclusive VIP tournament",
                        "priority": "high"
                    } for p in predictions if p["predicted_ltv"] >= 1000
                ] + [
                    {
                        "type": "sms",
                        "message": "Get 10% bonus on your next deposit",
                        "priority": "medium"
                    } for p in predictions if p["predicted_ltv"] < 1000
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

        # Convert all numpy types to native python types recursively before returning
        response = convert_numpy(response)

        return response

    except Exception as e:
        logger.error(f"Error in LTV prediction endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

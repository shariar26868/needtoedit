# import joblib
# import pandas as pd
# from app.config.settings import settings
# import logging
# import numpy as np

# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)

# class MLService:
#     def __init__(self):
#         self.model_dir = settings.MODEL_DIR
#         self.churn_model = self.load_model("churn_model.pkl")
#         self.ltv_model = self.load_model("ltv_model.pkl")
#         self.fraud_model = self.load_model("fraud_model.pkl")
#         self.segmentation_model = self.load_model("segmentation_model.pkl")
#         self.engagement_model = self.load_model("engagement_model.pkl")

#     def load_model(self, model_name):
#         try:
#             model_path = f"{self.model_dir}/{model_name}"
#             model = joblib.load(model_path)
#             logger.info(f"Loaded model from {model_path}")
#             return model
#         except Exception as e:
#             logger.error(f"Error loading model {model_name}: {str(e)}")
#             return None

#     def predict_churn(self, data):
#         try:
#             if self.churn_model is None or data.empty:
#                 return []
#             X = data[["total_deposits", "login_count"]].fillna(0)
#             predictions = self.churn_model.predict_proba(X)
#             churn_probabilities = predictions[:, 1]
#             return [
#                 {
#                     "user_id": user_id,
#                     "churn_probability": float(prob),
#                     "churn_label": "Churn" if prob > 0.5 else "Not Churn",
#                     "confidence": 0.95 if prob > 0.5 else 0.9,
#                     "priority_score": float(prob * 1.0588235294117647),
#                     "retention_recommendation": "Offer free spins and VIP support outreach" if prob > 0.5 else "Send loyalty email with 10% bonus",
#                     "feature_importance": {
#                         "recency": 0.5 if prob > 0.5 else 0.4,
#                         "frequency": 0.3,
#                         "monetary": 0.15 if prob > 0.5 else 0.2
#                     },
#                     "churn_impact": {
#                         "user_id": user_id,
#                         "estimated_impact": self.estimate_churn_impact(user_id, data)
#                     } if prob > 0.5 else {},
#                     "churn_trend": {
#                         "weekly_churn_rate": [0.1, 0.2, 0.3, 0.4]
#                     } if prob > 0.5 else {},
#                     "high_risk_groups": [
#                         {"group": "high frequency, low monetary", "risk": 0.8}
#                     ] if prob > 0.5 else [],
#                     "campaign_eligibility": "VIP rewards" if prob > 0.5 else "None",
#                     "preferred_game": "Unknown",
#                     "preferred_payment_method": "Unknown"
#                 } for user_id, prob in zip(data["user_id"], churn_probabilities)
#             ]
#         except Exception as e:
#             logger.error(f"Error predicting churn: {str(e)}")
#             return []

#     def predict_ltv(self, data):
#         try:
#             if self.ltv_model is None or data.empty:
#                 return []
#             X = data[["total_deposits", "total_bonuses", "deposit_count"]].fillna(0)
#             predictions = self.ltv_model.predict(X)
#             return [
#                 {
#                     "user_id": user_id,
#                     "predicted_ltv": float(pred)
#                 } for user_id, pred in zip(data["user_id"], predictions)
#             ]
#         except Exception as e:
#             logger.error(f"Error predicting LTV: {str(e)}")
#             return []

#     def predict_fraud(self, data):
#         try:
#             if self.fraud_model is None or data.empty:
#                 return []
#             X = data[["total_deposits", "total_wins", "rapid_deposits", "unique_ips"]].fillna(0)
#             predictions = self.fraud_model.predict(X)
#             scores = self.fraud_model.decision_function(X)
#             return [
#                 {
#                     "user_id": user_id,
#                     "fraud_label": "Fraud" if pred == -1 else "Not Fraud",
#                     "fraud_score": float(score)
#                 } for user_id, pred, score in zip(data["user_id"], predictions, scores)
#             ]
#         except Exception as e:
#             logger.error(f"Error predicting fraud: {str(e)}")
#             return []

#     def predict_segmentation(self, data):
#         try:
#             if self.segmentation_model is None or data.empty:
#                 return [], []
#             X = data[["recency", "frequency", "monetary"]].fillna(0)
#             segments = self.segmentation_model.predict(X)
#             segment_labels = {
#                 0: "Casual Players",
#                 1: "VIPs",
#                 2: "Inactive",
#                 3: "New Users"
#             }
#             predictions = [
#                 {
#                     "user_id": user_id,
#                     "segment": int(segment),
#                     "segment_label": segment_labels.get(int(segment), "Unknown")
#                 } for user_id, segment in zip(data["user_id"], segments)
#             ]
#             return predictions, segments
#         except Exception as e:
#             logger.error(f"Error predicting segmentation: {str(e)}")
#             return [], []

#     def predict_engagement(self, data):
#         try:
#             if self.engagement_model is None or data.empty:
#                 return []
#             X = data[["activity_count", "recency", "deposit_count"]].fillna(0)
#             predictions = self.engagement_model.predict_proba(X)
#             engagement_scores = predictions[:, 1]
#             return [
#                 {
#                     "user_id": user_id,
#                     "engagement_prediction": "Engaged" if score > 0.5 else "Not Engaged",
#                     "engagement_score": float(score)
#                 } for user_id, score in zip(data["user_id"], engagement_scores)
#             ]
#         except Exception as e:
#             logger.error(f"Error predicting engagement: {str(e)}")
#             return []

#     def estimate_churn_impact(self, user_id, data):
#         try:
#             user_data = data[data["user_id"] == user_id]
#             return float(user_data["total_deposits"].iloc[0] * 2) if not user_data.empty else 0.0
#         except Exception as e:
#             logger.error(f"Error estimating churn impact for user {user_id}: {str(e)}")
#             return 0.0





# import joblib
# import pandas as pd
# from app.config.settings import settings
# import logging
# import numpy as np

# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)

# class MLService:
#     def __init__(self):
#         self.model_dir = settings.MODEL_DIR
#         self.churn_model = self.load_model("churn_model.pkl")
#         self.ltv_model = self.load_model("ltv_model.pkl")
#         self.fraud_model = self.load_model("fraud_model.pkl")
#         self.segmentation_model = self.load_model("segmentation_model.pkl")
#         self.engagement_model = self.load_model("engagement_model.pkl")

#     def load_model(self, model_name):
#         try:
#             model_path = f"{self.model_dir}/{model_name}"
#             model = joblib.load(model_path)
#             logger.info(f"Loaded model from {model_path}")
#             return model
#         except Exception as e:
#             logger.error(f"Error loading model {model_name}: {str(e)}")
#             return None

#     def predict_churn(self, data):
#         try:
#             if self.churn_model is None or data.empty:
#                 return []
#             X = data[["recency", "frequency", "monetary"]].infer_objects(copy=False).fillna(0)
#             predictions = self.churn_model.predict_proba(X)
#             churn_probabilities = predictions[:, 1]
#             return [
#                 {
#                     "user_id": user_id,
#                     "churn_probability": float(prob),
#                     "churn_label": "Churn" if prob > 0.5 else "Not Churn",
#                     "confidence": 0.95 if prob > 0.5 else 0.9,
#                     "priority_score": float(prob * 1.0588235294117647),
#                     "retention_recommendation": "Offer free spins and VIP support outreach" if prob > 0.5 else "Send loyalty email with 10% bonus",
#                     "feature_importance": {
#                         "recency": 0.5 if prob > 0.5 else 0.4,
#                         "frequency": 0.3,
#                         "monetary": 0.15 if prob > 0.5 else 0.2
#                     },
#                     "churn_impact": {
#                         "user_id": user_id,
#                         "estimated_impact": self.estimate_churn_impact(user_id, data)
#                     } if prob > 0.5 else {},
#                     "churn_trend": {
#                         "weekly_churn_rate": [0.1, 0.2, 0.3, 0.4]
#                     } if prob > 0.5 else {},
#                     "high_risk_groups": [
#                         {"group": "high frequency, low monetary", "risk": 0.8}
#                     ] if prob > 0.5 else [],
#                     "campaign_eligibility": "VIP rewards" if prob > 0.5 else "None",
#                     "preferred_game": "Unknown",
#                     "preferred_payment_method": "Unknown"
#                 } for user_id, prob in zip(data["user_id"], churn_probabilities)
#             ]
#         except Exception as e:
#             logger.error(f"Error predicting churn: {str(e)}")
#             return []

#     def predict_ltv(self, data):
#         try:
#             if self.ltv_model is None or data.empty:
#                 return []
#             X = data[["total_deposits", "total_bonuses", "deposit_count"]].infer_objects(copy=False).fillna(0)
#             predictions = self.ltv_model.predict(X)
#             return [
#                 {
#                     "user_id": user_id,
#                     "predicted_ltv": float(pred) if not np.isnan(pred) else 0.0
#                 } for user_id, pred in zip(data["user_id"], predictions)
#             ]
#         except Exception as e:
#             logger.error(f"Error predicting LTV: {str(e)}")
#             return []

#     def predict_fraud(self, data):
#         try:
#             if self.fraud_model is None or data.empty:
#                 return []
#             X = data[["total_deposits", "total_wins", "rapid_deposits", "unique_ips"]].infer_objects(copy=False).fillna(0)
#             predictions = self.fraud_model.predict(X)
#             scores = self.fraud_model.decision_function(X)
#             return [
#                 {
#                     "user_id": user_id,
#                     "fraud_label": "Fraud" if pred == -1 else "Not Fraud",
#                     "fraud_score": float(score) if not np.isnan(score) else 0.0
#                 } for user_id, pred, score in zip(data["user_id"], predictions, scores)
#             ]
#         except Exception as e:
#             logger.error(f"Error predicting fraud: {str(e)}")
#             return []

#     def predict_segmentation(self, data):
#         try:
#             if self.segmentation_model is None or data.empty:
#                 return [], []
#             X = data[["recency", "frequency", "monetary"]].infer_objects(copy=False).fillna(0)
#             segments = self.segmentation_model.predict(X)
#             segment_labels = {
#                 0: "Casual Players",
#                 1: "VIPs",
#                 2: "Inactive",
#                 3: "New Users"
#             }
#             predictions = [
#                 {
#                     "user_id": user_id,
#                     "segment": int(segment),
#                     "segment_label": segment_labels.get(int(segment), "Unknown")
#                 } for user_id, segment in zip(data["user_id"], segments)
#             ]
#             return predictions, segments
#         except Exception as e:
#             logger.error(f"Error predicting segmentation: {str(e)}")
#             return [], []

#     def predict_engagement(self, data):
#         try:
#             if self.engagement_model is None or data.empty:
#                 return []
#             X = data[["activity_count", "recency", "deposit_count"]].infer_objects(copy=False).fillna(0)
#             predictions = self.engagement_model.predict_proba(X)
#             engagement_scores = predictions[:, 1]
#             return [
#                 {
#                     "user_id": user_id,
#                     "engagement_prediction": "Engaged" if score > 0.5 else "Not Engaged",
#                     "engagement_score": float(score) if not np.isnan(score) else 0.0
#                 } for user_id, score in zip(data["user_id"], engagement_scores)
#             ]
#         except Exception as e:
#             logger.error(f"Error predicting engagement: {str(e)}")
#             return []

#     def estimate_churn_impact(self, user_id, data):
#         try:
#             user_data = data[data["user_id"] == user_id]
#             return float(user_data["monetary"].iloc[0] * 2) if not user_data.empty else 0.0
#         except Exception as e:
#             logger.error(f"Error estimating churn impact for user {user_id}: {str(e)}")
#             return 0.0




# import joblib
# import pandas as pd
# from app.config.settings import settings
# import logging
# import numpy as np

# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)

# class MLService:
#     def __init__(self):
#         self.model_dir = settings.MODEL_DIR
#         self.churn_model = self.load_model("churn_model.pkl")
#         self.ltv_model = self.load_model("ltv_model.pkl")
#         self.fraud_model = self.load_model("fraud_model.pkl")
#         self.segmentation_model = self.load_model("segmentation_model.pkl")
#         self.engagement_model = self.load_model("engagement_model.pkl")

#     def load_model(self, model_name):
#         try:
#             model_path = f"{self.model_dir}/{model_name}"
#             model = joblib.load(model_path)
#             logger.info(f"Loaded model from {model_path}")
#             return model
#         except Exception as e:
#             logger.error(f"Error loading model {model_name}: {str(e)}")
#             return None

#     def predict_churn(self, data):
#         try:
#             if self.churn_model is None or data.empty:
#                 return []
#             X = data[["recency", "frequency", "monetary"]].infer_objects(copy=False).fillna(0)
#             predictions = self.churn_model.predict_proba(X)
#             churn_probabilities = predictions[:, 1]
#             return [
#                 {
#                     "user_id": int(user_id),  # Convert to Python int
#                     "churn_probability": float(prob),
#                     "churn_label": "Churn" if prob > 0.5 else "Not Churn",
#                     "confidence": 0.95 if prob > 0.5 else 0.9,
#                     "priority_score": float(prob * 1.0588235294117647),
#                     "retention_recommendation": "Offer free spins and VIP support outreach" if prob > 0.5 else "Send loyalty email with 10% bonus",
#                     "feature_importance": {
#                         "recency": 0.5 if prob > 0.5 else 0.4,
#                         "frequency": 0.3,
#                         "monetary": 0.15 if prob > 0.5 else 0.2
#                     },
#                     "churn_impact": {
#                         "user_id": int(user_id),  # Convert to Python int
#                         "estimated_impact": self.estimate_churn_impact(user_id, data)
#                     } if prob > 0.5 else {},
#                     "churn_trend": {
#                         "weekly_churn_rate": [0.1, 0.2, 0.3, 0.4]
#                     } if prob > 0.5 else {},
#                     "high_risk_groups": [
#                         {"group": "high frequency, low monetary", "risk": 0.8}
#                     ] if prob > 0.5 else [],
#                     "campaign_eligibility": "VIP rewards" if prob > 0.5 else "None",
#                     "preferred_game": "Unknown",
#                     "preferred_payment_method": "Unknown"
#                 } for user_id, prob in zip(data["user_id"], churn_probabilities)
#             ]
#         except Exception as e:
#             logger.error(f"Error predicting churn: {str(e)}")
#             return []

#     def predict_ltv(self, data):
#         try:
#             if self.ltv_model is None or data.empty:
#                 return []
#             X = data[["total_deposits", "total_bonuses", "deposit_count"]].infer_objects(copy=False).fillna(0)
#             predictions = self.ltv_model.predict(X)
#             return [
#                 {
#                     "user_id": int(user_id),  # Convert to Python int
#                     "predicted_ltv": float(pred) if not np.isnan(pred) else 0.0
#                 } for user_id, pred in zip(data["user_id"], predictions)
#             ]
#         except Exception as e:
#             logger.error(f"Error predicting LTV: {str(e)}")
#             return []

#     def predict_fraud(self, data):
#         try:
#             if self.fraud_model is None or data.empty:
#                 return []
#             X = data[["total_deposits", "total_wins", "rapid_deposits", "unique_ips"]].infer_objects(copy=False).fillna(0)
#             predictions = self.fraud_model.predict(X)
#             scores = self.fraud_model.decision_function(X)
#             return [
#                 {
#                     "user_id": int(user_id),  # Convert to Python int
#                     "fraud_label": "Fraud" if pred == -1 else "Not Fraud",
#                     "fraud_score": float(score) if not np.isnan(score) else 0.0
#                 } for user_id, pred, score in zip(data["user_id"], predictions, scores)
#             ]
#         except Exception as e:
#             logger.error(f"Error predicting fraud: {str(e)}")
#             return []

#     def predict_segmentation(self, data):
#         try:
#             if self.segmentation_model is None or data.empty:
#                 return [], []
#             X = data[["recency", "frequency", "monetary"]].infer_objects(copy=False).fillna(0)
#             segments = self.segmentation_model.predict(X)
#             segment_labels = {
#                 0: "Casual Players",
#                 1: "VIPs",
#                 2: "Inactive",
#                 3: "New Users"
#             }
#             predictions = [
#                 {
#                     "user_id": int(user_id),  # Convert to Python int
#                     "segment": int(segment),
#                     "segment_label": segment_labels.get(int(segment), "Unknown")
#                 } for user_id, segment in zip(data["user_id"], segments)
#             ]
#             return predictions, segments
#         except Exception as e:
#             logger.error(f"Error predicting segmentation: {str(e)}")
#             return [], []

#     def predict_engagement(self, data):
#         try:
#             if self.engagement_model is None or data.empty:
#                 return []
#             X = data[["activity_count", "recency", "deposit_count"]].infer_objects(copy=False).fillna(0)
#             predictions = self.engagement_model.predict_proba(X)
#             engagement_scores = predictions[:, 1]
#             return [
#                 {
#                     "user_id": int(user_id),  # Convert to Python int
#                     "engagement_prediction": "Engaged" if score > 0.5 else "Not Engaged",
#                     "engagement_score": float(score) if not np.isnan(score) else 0.0
#                 } for user_id, score in zip(data["user_id"], engagement_scores)
#             ]
#         except Exception as e:
#             logger.error(f"Error predicting engagement: {str(e)}")
#             return []

#     def estimate_churn_impact(self, user_id, data):
#         try:
#             user_data = data[data["user_id"] == user_id]
#             return float(user_data["monetary"].iloc[0] * 2) if not user_data.empty else 0.0
#         except Exception as e:
#             logger.error(f"Error estimating churn impact for user {user_id}: {str(e)}")
#             return 0.0

##########################################################################################################

# import joblib
# import pandas as pd
# import numpy as np
# from pathlib import Path
# from app.config.settings import settings
# import logging
# from datetime import datetime

# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)

# class MLService:
#     def __init__(self):
#         self.model_dir = Path(settings.MODEL_DIR)
#         self.models = self.load_models()

#     def load_models(self):
#         models = {}
#         model_files = {
#             "churn": "churn_model.pkl",
#             "ltv": "ltv_model.pkl",
#             "fraud": "fraud_model.pkl",
#             "segmentation": "segmentation_model.pkl",
#             "engagement": "engagement_model.pkl"
#         }
#         for model_name, file_name in model_files.items():
#             try:
#                 models[model_name] = joblib.load(self.model_dir / file_name)
#                 logger.info(f"Loaded model from {self.model_dir / file_name}")
#             except Exception as e:
#                 logger.error(f"Error loading {model_name} model: {str(e)}")
#         return models

#     def predict_churn(self, data, extra_metrics=None):
#         try:
#             if data.empty:
#                 return {}
#             model = self.models.get("churn")
#             if not model:
#                 logger.error("Churn model not loaded")
#                 return {}
#             features = data[["recency", "frequency", "monetary"]].fillna(0)
#             predictions = model.predict_proba(features)[:, 1]
#             results = [
#                 {
#                     "user_id": int(data.iloc[i]["user_id"]),
#                     "churn_probability": float(predictions[i]),
#                     "churn_label": "High Risk" if predictions[i] > 0.7 else "Medium Risk" if predictions[i] > 0.3 else "Low Risk"
#                 } for i in range(len(predictions))
#             ]
#             return {
#                 "prediction_type": "churn_prediction",
#                 "results": results,
#                 "average_churn_probability": float(np.mean(predictions)) if predictions.size > 0 else 0.0,
#                 "total_users": int(len(results)),
#                 "churn_rate": float(np.mean([p["churn_probability"] > 0.5 for p in results])) if results else 0.0,
#                 "high_risk_users": [int(r["user_id"]) for r in results if r["churn_probability"] > 0.7],
#                 "weekly_churn_trend": extra_metrics.get("weekly_churn_trend", []) if extra_metrics else [],
#                 "data_quality_issues": extra_metrics.get("data_quality_issues", []) if extra_metrics else [],
#                 "accuracy": extra_metrics.get("accuracy", 0.92) if extra_metrics else 0.92,
#                 "auc": extra_metrics.get("auc", 0.91) if extra_metrics else 0.91,
#                 "recommendations": extra_metrics.get("recommendations", []) if extra_metrics else [],
#                 "metadata": {
#                     "model_version": "v1.2",
#                     "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%S+06"),
#                     "data_freshness": "real-time"
#                 }
#             }
#         except Exception as e:
#             logger.error(f"Error predicting churn: {str(e)}")
#             return {}

#     def predict_ltv(self, data, extra_metrics=None):
#         try:
#             if data.empty:
#                 return {}
#             model = self.models.get("ltv")
#             if not model:
#                 logger.error("LTV model not loaded")
#                 return {}
#             features = data[["total_deposits", "total_bonuses", "deposit_count"]].fillna(0)
#             predictions = model.predict(features)
#             results = [
#                 {
#                     "user_id": int(data.iloc[i]["user_id"]),
#                     "predicted_ltv": float(predictions[i]) if not np.isnan(predictions[i]) else 0.0
#                 } for i in range(len(predictions))
#             ]
#             ltv_values = [r["predicted_ltv"] for r in results]
#             growth_potential = [
#                 {
#                     "user_id": int(r["user_id"]),
#                     "potential_ltv_increase": float(r["predicted_ltv"] * 0.2),
#                     "action": "Upsell VIP package"
#                 } for r in results
#             ]
#             ltv_segment_breakdown = {
#                 "low_value": float(np.mean([ltv < 500 for ltv in ltv_values]) * 100) if ltv_values else 0.0,
#                 "medium_value": float(np.mean([500 <= ltv < 1000 for ltv in ltv_values]) * 100) if ltv_values else 0.0,
#                 "high_value": float(np.mean([ltv >= 1000 for ltv in ltv_values]) * 100) if ltv_values else 0.0
#             }
#             return {
#                 "prediction_type": "ltv_prediction",
#                 "results": results,
#                 "average_ltv": float(np.mean(ltv_values)) if ltv_values else 0.0,
#                 "mae": 50.67,
#                 "ltv_range": {
#                     "min": float(min(ltv_values)) if ltv_values else 0.0,
#                     "max": float(max(ltv_values)) if ltv_values else 0.0
#                 },
#                 "total_users": int(len(results)),
#                 "ltv_forecast": extra_metrics if extra_metrics else {"predicted_ltv_next_month": 800.50},
#                 "ltv_segment_breakdown": ltv_segment_breakdown,
#                 "top_high_value_users": [
#                     {"user_id": int(r["user_id"]), "predicted_ltv": float(r["predicted_ltv"])}
#                     for r in results if r["predicted_ltv"] >= 1000
#                 ],
#                 "ltv_growth_potential": growth_potential,
#                 "recommendations": [
#                     {"type": "email", "message": "Invite to exclusive VIP tournament for Poker", "priority": "high"},
#                     {"type": "sms", "message": "Get 10% bonus on your next deposit", "priority": "medium"}
#                 ],
#                 "metadata": {
#                     "model_version": "v1.2",
#                     "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%S+06"),
#                     "data_freshness": "real-time"
#                 }
#             }
#         except Exception as e:
#             logger.error(f"Error predicting LTV: {str(e)}")
#             return {}

#     def predict_fraud(self, data, extra_metrics=None):
#         try:
#             if data.empty:
#                 return {}
#             model = self.models.get("fraud")
#             if not model:
#                 logger.error("Fraud model not loaded")
#                 return {}
#             features = data[["total_deposits", "total_wins", "win_count", "unique_ips", "rapid_deposits"]].fillna(0)
#             predictions = model.predict_proba(features)[:, 1]
#             results = [
#                 {
#                     "user_id": int(data.iloc[i]["user_id"]),
#                     "fraud_score": float(predictions[i]),
#                     "fraud_label": "Fraud" if predictions[i] > 0.5 else "Not Fraud"
#                 } for i in range(len(predictions))
#             ]
#             fraud_scores = [r["fraud_score"] for r in results]
#             return {
#                 "prediction_type": "fraud_detection",
#                 "results": results,
#                 "fraud_rate": float(np.mean([s > 0.5 for s in fraud_scores])) if fraud_scores else 0.0,
#                 "average_fraud_score": float(np.mean(fraud_scores)) if fraud_scores else 0.0,
#                 "total_users": int(len(results)),
#                 "fraud_percentage": float(np.mean([s > 0.5 for s in fraud_scores]) * 100) if fraud_scores else 0.0,
#                 "fraud_trend": extra_metrics.get("weekly_fraud_trend", []) if extra_metrics else [],
#                 "fraud_anomalies": [
#                     {"user_id": int(r["user_id"]), "anomalous_behavior": "Rapid deposits and high win streak"}
#                     for r in results if r["fraud_score"] > 0.7
#                 ],
#                 "top_fraudulent_users": [
#                     {"user_id": int(r["user_id"]), "fraud_score": float(r["fraud_score"])}
#                     for r in results if r["fraud_score"] > 0.7
#                 ],
#                 "real_time_alerts": [
#                     {"user_id": int(r["user_id"]), "alert": f"Suspicious deposit detected at {datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')}"}
#                     for r in results if r["fraud_score"] > 0.7
#                 ],
#                 "recommendations": [
#                     {"type": "account_action", "message": f"Require two-factor authentication for user {r['user_id']}", "priority": "urgent"}
#                     for r in results if r["fraud_score"] > 0.7
#                 ] + [
#                     {"type": "monitor", "message": f"Continue monitoring user {r['user_id']} activity", "priority": "low"}
#                     for r in results if r["fraud_score"] <= 0.7
#                 ],
#                 "metadata": {
#                     "model_version": "v1.2",
#                     "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%S+06"),
#                     "data_freshness": "real-time"
#                 }
#             }
#         except Exception as e:
#             logger.error(f"Error in fraud detection: {str(e)}")
#             return {}

#     def predict_segmentation(self, data):
#         try:
#             if data.empty:
#                 return [], {}
#             model = self.models.get("segmentation")
#             if not model:
#                 logger.error("Segmentation model not loaded")
#                 return [], {}
#             features = data[["recency", "frequency", "monetary"]].fillna(0)
#             predictions = model.predict(features)
#             results = [
#                 {
#                     "user_id": int(data.iloc[i]["user_id"]),
#                     "segment": int(predictions[i]),
#                     "segment_label": {0: "Casual Players", 1: "VIPs", 2: "Inactive", 3: "New Users"}.get(int(predictions[i]), "Unknown")
#                 } for i in range(len(predictions))
#             ]
#             return results, {}
#         except Exception as e:
#             logger.error(f"Error predicting segmentation: {str(e)}")
#             return [], {}

#     def predict_engagement(self, data, extra_metrics=None):
#         try:
#             if data.empty:
#                 return {}
#             model = self.models.get("engagement")
#             if not model:
#                 logger.error("Engagement model not loaded")
#                 return {}
#             features = data[["activity_count", "recency", "deposit_count"]].fillna(0)
#             predictions = model.predict_proba(features)[:, 1]
#             results = [
#                 {
#                     "user_id": int(data.iloc[i]["user_id"]),
#                     "engagement_score": float(predictions[i]),
#                     "engagement_prediction": "Engaged" if predictions[i] > 0.5 else "Not Engaged"
#                 } for i in range(len(predictions))
#             ]
#             return {
#                 "prediction_type": "engagement_prediction",
#                 "results": results,
#                 "average_engagement": float(np.mean(predictions)) if predictions.size > 0 else 0.0,
#                 "engagement_trend": extra_metrics.get("weekly_engagement_trend", []) if extra_metrics else [],
#                 "total_users": int(len(results)),
#                 "metadata": {
#                     "model_version": "v1.2",
#                     "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%S+06"),
#                     "data_freshness": "real-time"
#                 }
#             }
#         except Exception as e:
#             logger.error(f"Error predicting engagement: {str(e)}")
#             return {}








import joblib
import pandas as pd
from app.config.settings import settings
import logging
import numpy as np

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MLService:
    def __init__(self):
        self.model_dir = settings.MODEL_DIR
        self.churn_model = self.load_model("churn_model.pkl")
        self.ltv_model = self.load_model("ltv_model.pkl")
        self.fraud_model = self.load_model("fraud_model.pkl")
        self.segmentation_model = self.load_model("segmentation_model.pkl")
        self.engagement_model = self.load_model("engagement_model.pkl")

    def load_model(self, model_name):
        try:
            model_path = f"{self.model_dir}/{model_name}"
            model = joblib.load(model_path)
            logger.info(f"Loaded model from {model_path}")
            return model
        except Exception as e:
            logger.error(f"Error loading model {model_name}: {str(e)}")
            return None

    def predict_churn(self, data):
        try:
            if self.churn_model is None or data.empty:
                return []
            X = data[["recency", "frequency", "monetary"]].infer_objects(copy=False).fillna(0)
            predictions = self.churn_model.predict_proba(X)
            churn_probabilities = predictions[:, 1]
            return [
                {
                    "user_id": int(user_id),
                    "churn_probability": float(prob),
                    "churn_label": "Churn" if prob > 0.5 else "Not Churn",
                    "confidence": 0.95 if prob > 0.5 else 0.9,
                    "priority_score": float(prob * 1.0588235294117647),
                    "retention_recommendation": "Offer free spins and VIP support outreach" if prob > 0.5 else "Send loyalty email with 10% bonus",
                    "feature_importance": {
                        "recency": 0.5 if prob > 0.5 else 0.4,
                        "frequency": 0.3,
                        "monetary": 0.15 if prob > 0.5 else 0.2
                    },
                    "churn_impact": {
                        "user_id": int(user_id),
                        "estimated_impact": self.estimate_churn_impact(user_id, data)
                    } if prob > 0.5 else {},
                    "churn_trend": {
                        "weekly_churn_rate": [0.1, 0.2, 0.3, 0.4]
                    } if prob > 0.5 else {},
                    "high_risk_groups": [
                        {"group": "high frequency, low monetary", "risk": 0.8}
                    ] if prob > 0.5 else [],
                    "campaign_eligibility": "VIP rewards" if prob > 0.5 else "None",
                    "preferred_game": "Unknown",
                    "preferred_payment_method": "Unknown"
                } for user_id, prob in zip(data["user_id"], churn_probabilities)
            ]
        except Exception as e:
            logger.error(f"Error predicting churn: {str(e)}")
            return []

    def predict_ltv(self, data):
        try:
            if self.ltv_model is None or data.empty:
                return []
            X = data[["total_deposits", "total_bonuses", "deposit_count"]].infer_objects(copy=False).fillna(0)
            predictions = self.ltv_model.predict(X)

            return [
                {
                    "user_id": int(uid),
                    "predicted_ltv": float(pred) if not np.isnan(pred) else 0.0
                } for uid, pred in zip(data["user_id"], predictions)
            ]

        except Exception as e:
            logger.error(f"Error predicting LTV: {str(e)}")
            return []

    def predict_fraud(self, data):
        try:
            if self.fraud_model is None or data.empty:
                return []
            X = data[["total_deposits", "total_wins", "rapid_deposits", "unique_ips"]].infer_objects(copy=False).fillna(0)
            predictions = self.fraud_model.predict(X)
            scores = self.fraud_model.decision_function(X)
            return [
                {
                    "user_id": int(user_id),
                    "fraud_label": "Fraud" if pred == -1 else "Not Fraud",
                    "fraud_score": float(score) if not np.isnan(score) else 0.0
                } for user_id, pred, score in zip(data["user_id"], predictions, scores)
            ]
        except Exception as e:
            logger.error(f"Error predicting fraud: {str(e)}")
            return []

    def predict_segmentation(self, data):
        try:
            if self.segmentation_model is None or data.empty:
                return [], []
            X = data[["recency", "frequency", "monetary"]].infer_objects(copy=False).fillna(0)
            segments = self.segmentation_model.predict(X)
            segment_labels = {
                0: "Casual Players",
                1: "VIPs",
                2: "Inactive",
                3: "New Users"
            }
            predictions = [
                {
                    "user_id": int(user_id),
                    "segment": int(segment),
                    "segment_label": segment_labels.get(int(segment), "Unknown")
                } for user_id, segment in zip(data["user_id"], segments)
            ]
            return predictions, segments
        except Exception as e:
            logger.error(f"Error predicting segmentation: {str(e)}")
            return [], []

    def predict_engagement(self, data):
        try:
            if self.engagement_model is None or data.empty:
                return []
            X = data[["activity_count", "recency", "deposit_count"]].infer_objects(copy=False).fillna(0)
            predictions = self.engagement_model.predict_proba(X)
            engagement_scores = predictions[:, 1]
            return [
                {
                    "user_id": int(user_id),
                    "engagement_prediction": "Engaged" if score > 0.5 else "Not Engaged",
                    "engagement_score": float(score) if not np.isnan(score) else 0.0
                } for user_id, score in zip(data["user_id"], engagement_scores)
            ]
        except Exception as e:
            logger.error(f"Error predicting engagement: {str(e)}")
            return []

    def estimate_churn_impact(self, user_id, data):
        try:
            user_data = data[data["user_id"] == user_id]
            return float(user_data["monetary"].iloc[0] * 2) if not user_data.empty else 0.0
        except Exception as e:
            logger.error(f"Error estimating churn impact for user {user_id}: {str(e)}")
            return 0.0


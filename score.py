
import json
import joblib
import pandas as pd
from azureml.core.model import Model

def init():
    global model
    # Replace 'model.pkl' with the actual name of your registered model file if different
    model_path = Model.get_model_path('model')
    model = joblib.load(model_path)

def run(raw_data):
    try:
        # Load the JSON input and convert to a DataFrame
        input_data = json.loads(raw_data)
        data = pd.DataFrame(input_data['data'])
        
        # Define the expected feature columns (ensure these match the training features)
        feature_columns = [
            ' ROA(C) before interest and depreciation before interest',
            ' ROA(A) before interest and % after tax',
            ' ROA(B) before interest and depreciation after tax',
            ' Net Value Per Share (B)',
            ' Net Value Per Share (A)',
            ' Net Value Per Share (C)',
            ' Persistent EPS in the Last Four Seasons',
            ' Operating Profit Per Share (Yuan ¥)',
            ' Per Share Net profit before tax (Yuan ¥)',
            ' Debt ratio %',
            ' Net worth/Assets',
            ' Borrowing dependency',
            ' Operating profit/Paid-in capital',
            ' Inventory and accounts receivable/Net value',
            ' Working Capital to Total Assets',
            ' Current Liability to Assets',
            ' Working Capital/Equity',
            ' Current Liabilities/Equity',
            ' Retained Earnings to Total Assets',
            ' Total expense/Assets',
            ' Current Liability to Equity',
            ' Equity to Long-term Liability',
            ' Current Liability to Current Assets',
            ' Liability-Assets Flag',
            ' Net Income to Total Assets',
            " Net Income to Stockholder's Equity",
            ' Liability to Equity'
        ]
        
        # Select only the features needed for prediction
        data_features = data[feature_columns]
        
        # Make predictions with the loaded model
        result = model.predict(data_features).tolist()
        return json.dumps(result)
    except Exception as e:
        return json.dumps({"error": str(e)})

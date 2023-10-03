'''from django.shortcuts import render

import pandas as pd
import joblib  # Import the library you used to save your model

# Load the pre-trained machine learning model
loaded_model = joblib.load('C:\\Users\\grees\\anomaly_service\\anomaly_app\\model1.pkl')  # Replace with your model path

def input_form(request):
    is_anomaly = None

    if request.method == 'POST':
        input_data = pd.DataFrame({
            'T_Return': [float(request.POST['return_temp'])],
            'T_Outdoor': [float(request.POST['outdoor_temp'])],
            'RH_Outdoor': [float(request.POST['relative_humidity'])]
        })

        # Make predictions using the loaded model
        is_anomaly = loaded_model.predict(input_data)

        # Assuming the model predicts binary (0 for not anomaly, 1 for anomaly)
        #is_anomaly = bool(prediction[0])

        # Save the input data and prediction result to the database
        
        AnomalyData.objects.create(
            T_Return=input_data['return_temp'][0],
            T_Outdoor=input_data['outdoor_temp'][0],
            RH_Outdoor=input_data['relative_humidity'][0],
            is_anomaly=prediction
        )

    return render(request, 'input_form.html', {'is_anomaly': is_anomaly})
'''

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import joblib
import numpy as np
import pandas as pd
import json

# Load the pre-trained machine learning model
loaded_model = joblib.load('C:\\Users\\grees\\anomaly_service\\anomaly_app\\model1.pkl') 


@csrf_exempt
def predict_anomaly(request):
    if request.method == 'POST':
        # Parse the JSON data from the POST request
        data = json.loads(request.body)

        # Validate and preprocess the input data
        try:
            return_temp = float(data['return_temp'])
            outdoor_temp = float(data['outdoor_temp'])
            relative_humidity = float(data['relative_humidity'])

            # Create a DataFrame from the input data
            input_data = pd.DataFrame({
                'T_Return': [return_temp],
                'T_Outdoor': [outdoor_temp],
                'RH_Outdoor': [relative_humidity]
            })

            # Make predictions using the loaded model
            prediction = loaded_model.predict(input_data)

            # Convert the NumPy ndarray to a Python list
            prediction_list = prediction.tolist()

            # Return the prediction result as JSON response
            response_data = {'prediction': prediction_list}
            return JsonResponse(response_data)
        except (KeyError, ValueError):
            return JsonResponse({'error': 'Invalid input data'}, status=400)

    elif request.method == 'GET':
        # Handle GET request (e.g., provide usage instructions)
        response_data = {'message': 'Send a POST request with input data to get predictions.'}
        return JsonResponse(response_data)

    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
from django.shortcuts import render

def input_form(request):
    # Your view logic here
    return render(request, 'input_form.html')


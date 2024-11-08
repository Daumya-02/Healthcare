import joblib

# Path to the joblib model
model_path = 'Infectious_Disease_Prediction.joblib'  # Replace with actual filename

# Load the model
try:
    model = joblib.load(model_path)
    print("Model loaded successfully!")
except Exception as e:
    print("Error loading model:", e)

# Make a test prediction (replace with appropriate input data)
# try:
#     input_data = [[value1, value2, value3]]  # Replace with actual feature values
#     prediction = model.predict(input_data)
#     print("Prediction:", prediction)
# except Exception as e:
#     print("Error making prediction:", e)

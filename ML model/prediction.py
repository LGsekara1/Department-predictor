import numpy as np
import pandas as pd
import joblib
from keras.models import load_model

# Load the saved model, scaler, and encoder
model = load_model('department_allocation_model.h5')
scaler = joblib.load('scaler.pkl')
encoder = joblib.load('label_encoder.pkl')

# Function to predict the department for a new student
def predict_department(gpa, rank):
    # Create a DataFrame for the new input
    new_student = pd.DataFrame({'GPA': [gpa], 'Rank': [rank]})
    
    # Scale the input features
    new_student_scaled = scaler.transform(new_student)
    
    # Predict probabilities and decode the result
    predictions = model.predict(new_student_scaled)
    #print("predictions: ",predictions)
    predicted_classes = np.argsort(predictions, axis=1)[:,-3:][:,::-1]
    #print("predicted_classes: ",predicted_classes)
    predicted_probs = np.take_along_axis(predictions,predicted_classes,axis =1)
    #print("predicted_probs: ",predicted_probs)
    predicted_departments = encoder.inverse_transform(predicted_classes[0])
    #print("predicted_departments: ",predicted_departments)
    results_new = {dept:prob for dept,prob in zip(predicted_departments,predicted_probs[0])}
    #results = list(zip(predicted_departments,predicted_probs))

    return results_new




# Example input
gpa=input("Enter GPA: ")
rank = input("Enter rank: ")
results = predict_department(gpa,rank)
print("Predicted Departments with probabilities:")
for dept,prob in zip(results.keys(),results.values()):
    print(dept,round(prob,ndigits = 2))

from flask import Flask, request, jsonify
import joblib
import numpy as np
import tensorflow as tf
from flask_cors import CORS



#Loading presaved files 
model = tf.keras.models.load_model("department_allocation_model.h5")
scaler = joblib.load("scaler.pkl")
encoder = joblib.load("label_encoder.pkl")

#The flask aplication is initialized
app = Flask(__name__)
CORS(app)

#An API endpoint is created defining its route to only accept POST requests
@app.route("/predict",methods=["POST"])

def predict():
    try:
        #Extracting data from the JSON request which are the GPA and the Rank
        data=request.get_json()
        gpa,rank = data["GPA"],data["Rank"]

        #Preprocessing the data to present to the model as input
        new_student = np.array([gpa,rank])
        new_student_scaled = scaler.transform(new_student.reshape(1,-1))

        #Making the prediction using the pre-trained model
        predictions = model.predict(new_student_scaled)
        predicted_classes = np.argsort(predictions,axis =-1)[:,-3:][:,::-1]
        predicted_probs = np.take_along_axis(predictions,predicted_classes,axis = 1)
        predicted_departments = encoder.inverse_transform(predicted_classes[0])

        results = {dep:float(prob) for dep,prob in zip(predicted_departments,predicted_probs[0])}

        return jsonify(results)

    except Exception as e:
        return jsonify({"BackEndError":str(e)}),400
        #400 is the error code for bad HTTP Request

if __name__ =="__main__":
    app.run(debug=True)
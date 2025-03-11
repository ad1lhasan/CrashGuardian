import gradio as gr
import pickle
import numpy as np

knn = pickle.load(open("knn_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
label_encoders = pickle.load(open("label_encoders.pkl", "rb"))

def predict_survival(age, gender, speed, helmet, seatbelt):
    gender = label_encoders['Gender'].transform([gender])[0]
    helmet = label_encoders['Helmet_Used'].transform([helmet])[0]
    seatbelt = label_encoders['Seatbelt_Used'].transform([seatbelt])[0]
    
    input_data = scaler.transform([[age, gender, speed, helmet, seatbelt]])
    prediction = knn.predict(input_data)[0]
    
    return " Survived" if prediction == 1 else " Not Survived"

# Gradio Interface
iface = gr.Interface(
    fn=predict_survival,
    inputs=[gr.Number(label="Age"), 
            gr.Radio(["Male", "Female"], label="Gender"),
            gr.Number(label="Speed of Impact"), 
            gr.Radio(["Yes", "No"], label="Helmet Used"), 
            gr.Radio(["Yes", "No"], label="Seatbelt Used")],
    outputs=gr.Textbox(label="Prediction"),
    title="Accident Survival Prediction"
)

iface.launch()

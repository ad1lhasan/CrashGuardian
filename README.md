# CrashGuardian

## 🚀 Accident Survival Prediction using KNN
CrashGuardian is an AI-powered accident survival prediction tool that uses a K-Nearest Neighbors (KNN) model to estimate the likelihood of survival based on various factors such as age, gender, speed of impact, and protective gear usage.

## 📌 Features
- 🚗 Predicts survival probability in accidents.
- 🔍 Uses a trained KNN model for classification.
- 📊 Normalizes input data using a scaler for accurate predictions.
- 🎭 Encodes categorical variables with label encoding.
- 🌐 Interactive web interface powered by Gradio.

## 🛠️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ad1lhasan/CrashGuardian.git
   cd CrashGuardian
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```

## 📈 Usage
1. Open the Gradio web interface.
2. Input the required details:
   - Age
   - Gender (Male/Female)
   - Speed of Impact
   - Helmet Used (Yes/No)
   - Seatbelt Used (Yes/No)
3. Click "Predict" to get the survival prediction.

## 🗂 Project Structure
```
CrashGuardian/
│── app.py               # Gradio-based web application
│── knn_model.pkl        # Trained KNN model
│── scaler.pkl           # Scaler for input data normalization
│── label_encoders.pkl   # Encoders for categorical data
│── requirements.txt     # Dependencies list
│── README.md            # Project documentation
```

## 🤖 Technologies Used
- Python 🐍
- Gradio 🌍
- Scikit-learn 📊
- NumPy 🔢
- Pickle 🏗

## 📌 Contributing
Feel free to fork this repository and submit a pull request if you'd like to improve CrashGuardian!

## ⚠️ Disclaimer
This model provides **predictions** and should not be used as a replacement for medical or professional advice. Always prioritize real-world safety measures!

## 📜 License
This project is licensed under the MIT License.




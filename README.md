🌲🔥 Forest Fire Prediction – Machine Learning Project

This project predicts the Forest Fire Weather Index (FWI) using machine learning.
FWI helps determine the likelihood and intensity of forest fires based on various environmental and weather-related factors.

📂 Project Structure
Forest-Fire-Prediction/
│
├── Data/
│     ├── forest_fires.csv
│     ├── features_explanation.txt
│     └── other dataset files...
│
├── models/
│     ├── Ridge_Regression_Forest_Fire.pkl
│     ├── Standard_Scaler_Forest_Fire.pkl
│
├── templates/
│     ├── home.html
│     └── index.html
│
├── app.py
├── README.md
└── requirements.txt

📊 Dataset Description (located in Data/)

The dataset contains multiple inputs used to predict the Forest Fire Weather Index (FWI).
These include weather conditions, moisture indices, and fire spread indicators.

Feature	Description
Temperature	Temperature in °C
RH	Relative Humidity (%)
Ws	Wind Speed (km/h)
Rain	Rainfall (mm)
FFMC	Fine Fuel Moisture Code
DMC	Duff Moisture Code
ISI	Initial Spread Index
Classes	Fire severity class (numeric or encoded)
Region	Region of observation (encoded)

The target variable is:

FWI — Forest Fire Weather Index
🧠 Machine Learning Model

The project uses:

Ridge Regression for predicting continuous FWI values

StandardScaler for feature scaling

Both the scaler and trained model are stored inside the models/ folder.

🚀 How to Run This Project
1. Clone the repository
git clone https://github.com/Naman0911/Forest-Fire-Prediction.git
cd Forest-Fire-Prediction

2. Install required Python packages
pip install -r requirements.txt

3. Run the Flask application
python app.py

4. Open the web app
http://127.0.0.1:5000/

🖥️ Web Interface Features

The web interface allows the user to enter the following values:
Temperature
RH
Wind Speed
Rain
FFMC
DMC
ISI
Classes
Region
After submitting the form, the model predicts the Forest Fire Weather Index (FWI) and displays it on the screen.

📦 Requirements

All dependencies are listed in:
requirements.txt


Install using:
pip install -r requirements.txt

📈 Future Enhancements

Add visualizations for prediction outputs
Include more advanced models (Random Forest, XGBoost)
Deploy the app on cloud platforms
Add a fire risk classification system (Low, Medium, High)

🤝 Contributing

Contributions are welcome!
If you want to suggest improvements, feel free to open an issue or submit a pull request.

📧 Contact

Author: Naman Upadhyay
GitHub: Naman0911
